@echo off
REM ���O�t�@�C���̃f�B���N�g���ƃt�@�C������ݒ�
mkdir log
set log_file=log\%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%.log

REM ���O�̊J�n�������t�@�C���ɋL�^
echo �J�n����: %date% %time% > %log_file%

REM Python�̉��z����L���ɂ���
call .venv\Scripts\activate

REM Python �X�N���v�g�����s���A�o�͂����O�t�@�C���ɒǉ��i�R���\�[���ɂ��o�́j
python . >> %log_file%

REM ���O�̏I���������t�@�C���ɋL�^
echo �I������: %date% %time% >> %log_file%
