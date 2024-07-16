from typing import List, Optional
from pydantic import BaseModel, UUID4, HttpUrl


class Metadata(BaseModel):
    tags: str
    prompt: str
    gpt_description_prompt: str
    audio_prompt_id: Optional[UUID4]
    history: Optional[str]
    concat_history: Optional[str]
    type: str
    duration: float
    refund_credits: bool
    stream: bool
    infill: Optional[str]
    has_vocal: Optional[str]
    is_audio_upload_tos_accepted: Optional[bool]
    error_type: Optional[str]
    error_message: Optional[str]


class Clip(BaseModel):
    id: UUID4
    video_url: HttpUrl
    audio_url: HttpUrl
    image_url: HttpUrl
    image_large_url: HttpUrl
    is_video_pending: bool
    major_model_version: str
    model_name: str
    metadata: Metadata
    is_liked: bool
    user_id: UUID4
    display_name: str
    handle: str
    is_handle_updated: bool
    avatar_image_url: HttpUrl
    is_trashed: bool
    reaction: Optional[str]
    created_at: str
    status: str
    title: str
    play_count: int
    upvote_count: int
    is_public: bool


class Feed(BaseModel):
    clips: List[Clip]
    num_total_results: int
    current_page: int
