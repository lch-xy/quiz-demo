<img width="976" alt="image" src="https://github.com/lch-xy/quiz-demo/assets/39256937/4c378960-edc0-4cf4-863f-1923385dc8c0">
<img width="1066" alt="image" src="https://github.com/lch-xy/quiz-demo/assets/39256937/2a085e78-e4a1-45d1-ae45-f44c039f10a3">

单词可以从墨墨单词的安卓安装包的 assets 文件夹里找 maimemo.v3.db 文件

```sql
  SELECT
      chapter_origin_id,
      voc_origin_id,
      title,
      spelling
  FROM
      VOC_TB
          INNER JOIN (
          SELECT
              title,
              voc_origin_id,
              chapter_origin_id
          FROM
              BK_VOC_TB AS V
                  INNER JOIN BK_CHAPTER_TB AS C ON V.chapter_origin_id = C.id
                  AND V.book_origin_id IN ( ( SELECT origin_id FROM BK_TB WHERE name like '雅思热词酷听力1500词' ) )
      ) AS tmp ON VOC_TB.origin_id = tmp.voc_origin_id
```
