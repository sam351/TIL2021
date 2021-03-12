# 데이터 모델링(Data Modeling) 정의

- **모델(Model)** : 어떤 목적을 가지고 진짜를 모방한 것

​       따라서, 좋은 모델은 목적에 부합하는 모방



- 모델링의 궁극적 목적은 컴퓨터의 데이터베이스에 있는 표에 정보를 담는 것

​       이를 통해 거대한 양의 정보를 신속하게 처리할 수 있음



- 무한히 거대하고 복잡한 현실을 정보로 만들어서 표에 담는 것은 매우 어려운 작업

​       이 작업을 쉽게 할 수 있도록 수립된 방법론이 데이터 모델링(Data Modeling)





# 데이터 모델링의 전체 흐름

![image-20210312134430180](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210312134430180.png)

**1.  업무 파악**

- 모델링을 의뢰한 사람의 업무 및 요구사항을 파악하는 단계
- 산출물 : 모델링 기획서



**2. 개념적 데이터 모델링**

- 현실의 업무를 뜯어내서 개념을 찾아내는 단계
- 산출물 : ERD (Entity Relationship Diagram)



**3. 논리적 데이터 모델링**

- 앞에서 찾아낸 개념을 관계형 데이터베이스에 맞게 표로 재구성하는 단계



**4. 물리적 데이터 모델링**

- 적절한 데이터베이스 제품을 선택하고, 해당 제품에 최적화된 코드를 작성해서 실제 표를 만드는 단계
- 산출물 : 표를 생성하는 SQL 코드



**결론** : 데이터 모델링이란 문제를 현실로부터 뜯어 내고, 고도의 추상화 과정을 거쳐서, 그것을 컴퓨터라는 새로운 현실로 옮겨 담는 작업

현실과 컴퓨터 세계는 크게 다르기 때문에, 처음에 해결하려고 했던 문제가 데이터베이스의 표에 잘 담겼는지를 확인하는 작업이 끊임없이 계속되어야 함





# 1단계. 업무파악

- 컴퓨터 프로그램을 만들기 위해서는 업무에 대해 명확하게 이해하는 것이 필요함

​       이를 위해 실무자와 정확하게 소통하는 것이 중요함

- 실무자들은 업무에 대한 정확한 이해 없이 익숙해져서 일을 잘하는 것일 수 있음

​       이해를 했다면 설명할 수 있어야 하며, 설명할 수 없다면 이해 없이 익숙해진 상태로 일을 잘 하는 것일 뿐임

- 업무에 익숙해진 사람으로부터 필요한 정보를 끌어내기 위해서는 많은 노하우와 노력이 필요함
- 업무파악에 효과적인 방법론 중 하나는 UI를 함께 그려보는 것

​       이를 통해 서로가 원하는 방향을 효율적으로 일치시킬 수 있음

​       말/글로는 서로가 원하는 방향을 명확하게 하기 상대적으로 어려움



### 기획서 샘플

- 활용 오픈소스 툴 : Oven

![image-20210309153637030](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210309153637030.png)





# 2단계. 개념적 데이터 모델링

- 개념적 데이터 모델링 : 파악한 업무로부터 개념을 뽑아내는 작업

- ERD - 그룹, 정보/데이터, 관계
- 개념(ex. 글, 댓글, 저자) : **Entity** → 이후 **table**로 전환
- 개념을 구성하는 실제 데이터(ex. 글을 구성하는 구체적 데이터는 제목, 생성일, 본문) : **Attribute(속성)** → 이후 **column**으로 전환
- 개념 간의 관계(ex. 댓글은 글에 소속, 저자는 글/댓글을 작성) : **Relation(관계)** → 이후 **PK(기본키), FK(외래키)**로 전환

+추가 개념 - table을 구성하는 각 행 : **Tuple**



### Cardinality

- 최대로 대응시킬 수 있는 인스턴스 수 정보
- 1:1(일대일) - 담임은 반을 한 개만 맡을 수 있고, 반은 담임을 한 명만 가질 수 있음
- 1:N(일대다) - 저자는 댓글을 여러 개 작성할 수 있고, 댓글은 저자를 한 명만 가질 수 있음
- N:M(다대다) 관계 - 저자는 글을 여러 개 작성할 수 있고, 글은 저자를 여러 명 가질 수 있음
  - N:M의 경우 데이터베이스에서 바로 구현이 불가능해, 중간에 매개하는 테이블 구현 필요



### Optionality

- 인스턴스 대응이 필수적인지 여부 정보 (최소로 대응시킬 수 있는 인스턴스 수 정보)
- 저자는 댓글을 반드시 작성할 필요 없지만, 댓글은 저자를 반드시 가져야 함



### ERD 샘플

- 활용 오픈소스 툴 : drawio

![image-20210309153231441](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210309153231441.png)





# 3단계. 논리적 데이터 모델링

- 이전 단계인 개념적 데이터 모델링이 업무에서 개념(entity)들을 뽑아내는 일이라면, 논리적 데이터 모델링은 그 개념(entity)들을 관계형 데이터베이스 패러다임에 어울리게 데이터 형식을 잘 정립하는 일
- 구체적 데이터베이스 제품의 특성이나 성능 등은 크게 신경쓰지 않으며, 관계형 데이터베이스 패러다임에 어울리는 가장 이상적인 모습으로 정리하는 것이 주 목적

![image-20210309153043459](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210309153043459.png)



### 산출물 샘플

- 활용 오픈소스 툴 : ER Master

![image-20210310133538832](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210310133538832.png)





# 3단계. 논리적 데이터 모델링 - 정규화

- 정규화(Normalization) : 정제되지 않은 데이터(표)를 관계형 데이터베이스에 어울리는 데이터(표)로 만들어주는 작업
- 1~3차 정규화 사례 (http://bit.ly/2wV2SFj)



### 제1정규화

- 제1정규화의 원칙은 Atomic columns - 테이블 내 각 셀의 값이 atomic(원자적)해야 함

  ex) tag 컬럼 안에 rdb, free, commercial 와 같은 값이 들어있다면 하나 이상의 여러 값이 동시에 들어 있으므로 atomic 하지 않음

- 각 셀이 여러 값을 갖는 컬럼의 경우, 별도의 테이블로 분리시킨 다음 N:M 관계로 연결시켜 주는 것이 타당 (매핑 테이블 사용)

- 제1정규화 샘플

  ![image-20210310142630545](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210310142630545.png)



### 제2정규화

- 제2정규화의 원칙은 No partial dependencies - 부분 종속성(partial dependencies)이 없어야 함

  ex) 테이블에서 도서(title)별 상세정보가 중복되어 저장된 경우, 부분 종속성이 발생한 것이므로 도서별 상세정보를 중복 없이 저장하는 별도 테이블로 분리시켜야 함

- 테이블의 기본키(primary key) 중 중복키인 것이 없어야 함

- 제2정규화 샘플

  ![image-20210310162326114](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210310162326114.png)



### 제3정규화

- 제3정규화의 원칙은 No transitive dependencies - 이행적 종속성(transitive dependencies)이 없어야 함

  ex) 제2정규화 결과물에서 author_name, author_profile은 title(pk)이 아닌 author_id에 의존하고 있으므로 이행적 종속성이 존재함

- 실제 데이터에서는 author_id처럼 이행적 종속성을 명시적으로 드러내는 단서가 잘 없을 수도 있음

  이 경우 서로 성격이 같은 컬럼들(암식적으로 식별자를 가진 컬럼들)을 찾아내려는 노력 필요

- 제3정규화 샘플

  ![image-20210312134148683](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210312134148683.png)





# 4단계. 물리적 데이터 모델링

- 이전 단계인 논리적 데이터 모델링이 관계형 데이터베이스에 맞는 이상적인 표를 만드는 것이라면, 물리적 데이터 모델링은 이상적인 표를 구체적인 제품에 맞는 현실적 표로 만드는 것
- 이 단계에서 중요한 것은 성능임
- 데이터베이스 제품별로 find slow query 관련 기능을 사용하면, 특별히 성능을 떨어뜨리는 query를 식별하기 용이함
- **역정규화(denormalization) 또는 반정규화** : 쿼리 성능을 높이기 위해, 이상적으로 정규화된 테이블 구조를 변경하는 것
- 역정규화 사례 (http://bit.ly/2WLMCko)
- 역정규화 이전에 먼저 시도해 볼 수 있는 성능 향상 방안은 **index**(행별 읽기 성능을 비약적으로 향상시키지만, 쓰기 성능을 희생함), **cache**(쿼리 실행 결과를 저장했다가 동일한 쿼리가 들어왔을 때 사용) 등이 있음



#### 1. 역정규화(denormalization) - 컬럼을 조작해서 join 줄이기

- ex. 도서(topic_title)별 태그명(tag_name)을 확인하는 경우가 많을 때

- 매번 JOIN을 수행하는 것은 성능을 저하시키므로, 의도적으로 중복을 허용하는 컬럼 추가

  ![image-20210312155833875](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210312155833875.png)



#### 2. 역정규화(denormalization) - 파생컬럼을 형성해 계산작업 줄이기

- ex. 저자(author_id)별 도서 수(topic_count)를 최신 상태로 유지하고 싶을 때

- 매번 GROUP BY를 수행하는 것은 성능을 저하시키므로, 연산 결과를 저장하는 컬럼 추가한 뒤 매번 도서(topic) 테이블에 row가 추가될 때 해당하는 topic_count를 1씩 증가

  ![image-20210312160009024](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210312160009024.png)



#### 3. 역정규화(denormalization) - 표를 쪼개기

- ex. 전체 데이터가 너무 크거나, 자주 사용하는 column/row가 정해져 있을 때

- 표를 column 또는 row 단위로 쪼개어 데이터 저장 및 query 처리를 병렬화

  ![image-20210312160407107](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210312160407107.png)



#### 4. 역정규화(denormalization) - 관계의 역정규화

- ex. 저자(author_id)별 태그명(tag_name)을 확인하는 경우가 많을 때
- 매번 topic, topic_tag_relation, tag 테이블을 모두 JOIN해야 하므로, 역정규화를 통해 JOIN 줄이기

![image-20210312160448913](C:\Users\dslab01\AppData\Roaming\Typora\typora-user-images\image-20210312160448913.png)



