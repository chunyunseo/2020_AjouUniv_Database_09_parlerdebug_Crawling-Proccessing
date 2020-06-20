2020년 아주대학교 정태선 교수님의 최종보고서에 들어가는 코드입니다.
조원:
소프트웨어학과 201520882 천윤서
소프트웨어학과 201520993 정  욱
소프트웨어학과 201520998 정원종
소프트웨어학과 201521001 정찬호

파일 및 리포지터리 설명:
2020_AjouUniv_Database_09_parlerdebug_Main_Application
안드로이드와 Sqlite로 개발된 응용 어플리케이션입니다.


2020_AjouUniv_Database_09_parlerdebug_Crawling+Proccessing:
크롤링과 데이터 처리에 쓰인 코드를 지니고 있는 리포지터리입니다.

TupleData:
Insert할 데이터를 \t와 \n으로 가볍게 구분하고 있는 상태의 튜플입니다.

ConvertTxtFileToInsertQuery.py:
TupleData를 파싱해서 Insert 쿼리문으로 반환해주는 파일입니다.

Crawling.py
동식물에 관한 정보를 수집하는 크롤러입니다.

Dataprocessing.py:
크롤링한 데이터들을 \t와 \n으로 구분된 튜플들로 파싱해주는 파일입니다.
