## READ ME

```sql
CREATE TABLE movies ();
-- movies라는 테이블을 생성한다.
SELECT * FROM movies;
-- movies에 있는 내용을 모두 가져온다
INSERT INTO movies VALUES (20182530,'극한직업','15세이상관람가','이병헌','20190123',3138467,111,'한국','코미디');
--  movies 테이블에 values 값이 있는 row를 movies에 추가한다.
DELETE FROM movies WHERE 영화코드=20040521;
-- 영화코드가 20040521인 row를 movies에서 제거한다
UPDATE movies SET 감독='없음' WHERE 영화코드=20185124;
-- 영화코드가 20185124인 row에서 감독 column의 값을 없음으로 변경한다
SELECT * FROM movies WHERE 상영시간>=150;
-- 상영시간이 150분 이상인 영화출력
SELECT 영화이름 FROM movies WHERE 장르='애니메이션' AND 제작국가='덴마크';
--장르는 애니메이션 제작국가는 덴마크인 영화이름만 출력한다
SELECT SUM(누적관객수) FROM movies;
-- 누적관객수를 전체 합한 값을 출력한다
SELECT COUNT(관람등급) FROM movies WHERE 관람등급='청소년관람불가';
--청소년 관람불가인 영화의 수를 출력한다.
ORDER BY column 
-- column을 기준으로 오름차순 정렬한다
ORDER BY column DESC
-- column을 기준으로 내림차순 정렬한다
LIMIT 5
-- 5개만 출력한다.
```

