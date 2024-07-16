import streamlit as st
from main import i18n

from cookie import new_suno_auth
from sqlite import SqliteTool

suno_sqlite = SqliteTool()

main_col, _,_ = st.columns(3)
placeholder = main_col.empty()

container1 = main_col.container(border=True)

# 设置信息
st.session_state.Setting = False
Setting = container1.toggle(i18n("Setting"))

identity = ""
Session = ""
Cookie = ""

# 设置
if Setting:
    st.session_state.Setting = True
    # print(st.session_state.Setting)

    if "Identity" not in st.session_state:
        pass
    else:
        identity = st.session_state.Identity

    # 查询数据库
    result = suno_sqlite.query_one("select id,identity,[session],cookie from session where identity =?", (identity,))
    print(result)
    print("\n")
    if result:
        # 如果存在则直接使用
        identity = result[1]
        Session = result[2]
        Cookie = result[3]
        
    Identity = container1.text_input(label="Identity:", value=identity, placeholder=i18n("Identity Placeholder"), max_chars=50, help=i18n("Identity Help"))
    st.session_state.Identity = Identity
    # print(st.session_state.Identity)
    Session = container1.text_input(label="Session:", value=Session, placeholder=i18n("Session Placeholder"),max_chars=50, help=i18n("Session Help"))
    st.session_state.Session = Session
    # print(st.session_state.Session)
    Cookie = container1.text_area(label="Cookie:", value=Cookie, placeholder=i18n("Cookie Placeholder"), height=150, max_chars=2000, help=i18n("Cookie Help"))
    st.session_state.Cookie = Cookie
    # print(st.session_state.Cookie)

    st.session_state.SaveInfo = False
    SaveInfo = container1.button(i18n("SaveInfo"))
    if SaveInfo:
        st.session_state.SaveInfo = True
        if Identity == "":
            placeholder.error(i18n("SaveInfo Identity Error"))
        elif Session == "":
            placeholder.error(i18n("SaveInfo Session Error"))
        elif Cookie == "":
            placeholder.error(i18n("SaveInfo Cookie Error"))
        elif len(Cookie) < 500:
            placeholder.error(i18n("SaveInfo Cookie Error"))
        else:
            result = suno_sqlite.query_one("select id,identity,[session],cookie from session where identity =?", (Identity,))
            print(result)
            print("\n")
            if result:
                result = suno_sqlite.operate_one("update session set session=?, cookie=?, token=? where identity =?", (Session, Cookie, Identity,""))
            else:
                result = suno_sqlite.operate_one("insert into session (identity,session,cookie,token) values(?,?,?,?)", (Identity, Session, Cookie,""))

            if result:
                st.session_state.Identity = Identity
                # 创建新的suno认证
                new_suno_auth(Identity, Session, Cookie)
                # print(st.session_state.Identity)
                placeholder.empty()
                main_col.success(i18n("SaveInfo Success"))
            else:
                placeholder.error(i18n("SaveInfo Error"))
            print(result)
            print("\n")
            # print(st.session_state.SaveInfo)
    else:
        st.session_state.SaveInfo = False
        # print(st.session_state.SaveInfo)

st.session_state.token = ""
st.session_state.suno_auth = None
