# -*- coding:utf-8 -*-

from datetime import datetime
from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field

class CustomModeGenerateParam(BaseModel):
    """Generate with Custom Mode"""

    prompt: str = Field(..., description="lyrics")
    mv: str = Field(
        ...,
        description="model version, default: chirp-v3-0",
        examples=["chirp-v3-0"],
    )
    title: str = Field(..., description="song title")
    tags: str = Field(..., description="style of music")
    continue_at: Optional[str] = Field(
        default=None,
        description="continue a new clip from a previous song, format mm:ss",
        examples=["01:23"],
    )
    continue_clip_id: Optional[str] = None


class DescriptionModeGenerateParam(BaseModel):
    """Generate with Song Description"""

    gpt_description_prompt: str
    make_instrumental: bool = False
    mv: str = Field(
        ...,
        description="model version, default: chirp-v3-0",
        examples=["chirp-v3-0"],
    )
    prompt: str = Field(
        default="",
        description="Placeholder, keep it as an empty string, do not modify it",
    )

class LyricsGenerateParam(BaseModel):
    """Generate with Song Lyrics"""
    prompt: str = Field(
        default="Someone who is passionate about work and life.",
    )


from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime
from uuid import UUID

class MetaData(BaseModel):
    tags: str
    prompt: str
    gpt_description_prompt: str
    audio_prompt_id: Optional[Any]
    history: Optional[Any]
    concat_history: Optional[Any]
    type: str
    duration: float
    refund_credits: bool
    stream: bool
    infill: Optional[Any]
    has_vocal: Optional[Any]
    is_audio_upload_tos_accepted: Optional[Any]
    error_type: Optional[Any]
    error_message: Optional[Any]

class Music(BaseModel):
    id: UUID
    video_url: str
    audio_url: str
    image_url: str
    image_large_url: str
    is_video_pending: bool
    major_model_version: str
    model_name: str
    metadata: MetaData
    is_liked: bool
    user_id: UUID
    display_name: str
    handle: str
    is_handle_updated: bool
    avatar_image_url: str
    is_trashed: bool
    reaction: Optional[Any]
    created_at: datetime
    status: str
    title: str
    play_count: int
    upvote_count: int
    is_public: bool
