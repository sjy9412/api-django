```bash
$ pip install djangorestframework
```

```python
INSTALLED_APPS = [
    'rest_framework',
    ...
	]
```

```bash
$ python manage.py dumpdata --indent 2 musics > musics.json
```

* dumpdata를 json파일로 만들어줌





# http

* GET reviews/ 리뷰 목록
* POST reviews/ 리뷰 등록하기
* GET reviews/1/ 1번 리뷰 가져오기
* PUT reviews/1/ 1번 리뷰 수정하기
* DELETE reviews/1/ 1번 리뷰 삭제하기



## Interface

* GUI (Graphic user interface)
  * 그래픽 - 유저랑 상호작용하는 인터페이스
* CLI(Command Line Interface)
  * 명령어 인터페이스
* API(Application programming interface)
  * 프로그래밍으로 인터페이스



# validators

```python
from django.core.validators import MinValueValidator

class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(
    	validators=[MinValueValidator(20, message='미성년자 출입 금지')])
```

* 특정 데이터만 접근 할 수 있도록
* 모델 form에 넣으면 `.clean_fields()`로 확인 가능