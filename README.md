# Django를 이용한 게시판
## 기본 메인화면
- 주소 입력시 가장 먼저 보여지는 페이지
- 비로그인시 상단에 로그인 버튼을 출력, 로그인시 UserID(로그아웃)을 출력
- 로그인 후 글쓰기 버튼을 누르면 글작성(create) 페이지로 이동, 비로그인시 로그인 화면으로 이동

![1](https://user-images.githubusercontent.com/78770258/141659101-fb526139-9eba-4048-b1aa-893ac4f6514c.JPG)
## 정렬
- GET방식으로 요청하여 정렬과 필터, 검색, 페이징을 동시에 동작이 가능
- html 파일에서 searchForm 에 select 값이 요청될 때마다 값을 저장하는 Javascript 작성하고, 그 값을 index 함수에 전송받아 각각 최신, 추천, 답변, 인기순으로 정렬

![2](https://user-images.githubusercontent.com/78770258/141660860-a16c32b5-f0ff-4400-80df-509219823cdd.JPG)
## 필터 검색
- 정렬 방식과 비슷하게 select 값을 searchForm 에 전송하여 검색어(kw)를 입력 받을 때마다 해당 필터(tp) 값을 비교 후 제목, 내용, 제목 + 내용, 글쓴이 기준으로 검색

![3](https://user-images.githubusercontent.com/78770258/141660876-9fd0bd28-170d-4a28-aa9f-ad51d12b42af.JPG)
## 게시글 상세페이지
- 제목과 내용, 답변, 댓글을 정렬한 페이지
- 글쓴이와 작성날짜, 추천 및 조회수를 나타내며 글을 수정시 작성일 옆에 수정한 날짜를 출력
- 사용자와 글쓴이가 일치하면 수정 및 삭제 버튼을 출력
- model에 ManyToManyField를 사용하여 추천 속성을 추가
- views의 추천함수(vote)에 현재 사용자와 데이터 값을 비교하여 본인이 작성한 글 혹은 이미 추천한 글에는 오류를 출력
- 로그인 상태가 아니면 답변등록 폼을 비활성화

![4](https://user-images.githubusercontent.com/78770258/141660800-02782799-7da7-49fa-9525-2bf21dab26ac.JPG)
## 관리 페이지
- 슈퍼유저 권한이 있는 회원만 접근이 가능
- 게시글, 유저, 최근 활동 등 관리하는 페이지

![5](https://user-images.githubusercontent.com/78770258/141659294-25b1f9ae-3943-47c2-a068-700f154b5eec.JPG)
