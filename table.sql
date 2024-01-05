-- auto-generated definition
create table vocabulary_words
(
    id               bigint auto_increment comment '编号'
        primary key,
    ch_example       text          null comment '中文例子',
    en_example       text          null comment '英文例子',
    review_cnt       int default 0 null comment '复习次数',
    success          int default 0 null comment '成功',
    failure          int default 0 null comment '失败',
    last_review_date datetime      null comment '最后复习时间',
    constraint sentence_id_uindex
        unique (id)
)
    comment '单词';

-- auto-generated definition
create table speaking_phrases
(
    id               bigint auto_increment comment '编号'
        primary key,
    ch_example       text          null comment '中文例子',
    en_example       text          null comment '英文例子',
    review_cnt       int default 0 null comment '复习次数',
    success          int default 0 null comment '成功',
    failure          int default 0 null comment '失败',
    last_review_date datetime      null comment '最后复习时间',
    constraint sentence_id_uindex
        unique (id)
)
    comment '口语';

-- auto-generated definition
create table writing_phrases
(
    id               bigint auto_increment comment '编号'
        primary key,
    ch_example       text          null comment '中文例子',
    en_example       text          null comment '英文例子',
    review_cnt       int default 0 null comment '复习次数',
    success          int default 0 null comment '成功',
    failure          int default 0 null comment '失败',
    last_review_date datetime      null comment '最后复习时间',
    constraint sentence_id_uindex
        unique (id)
)
    comment '写作';

