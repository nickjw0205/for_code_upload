Controller.py를 실행하시면 됩니다.
맨 처음에 제일 상단에 Level(라디오 버튼)을 누르시고 start버튼을 누르시면 게임이 시작됩니다.
구멍의 수는 Hard = 40, Normal = 34, Easy = 28개입니다.
 
그 후 입력하고자하는 좌표값을 x,y에 넣고 num에 답을 적으시면됩니다.
input 버튼을 누르면 답을 제출하는 것이고
Memo는 점수에 상관없이 num을 메모하고자 하는 것입니다.
어떤 num을 넣어야 할지 모르겠으면 ? 버튼을 누르시면 됩니다.

Save는 현재 스코어와 보드를 각각 score.txt, board.txt에저장하는 기능이고
Load는 score.txt, board.txt에서 이전에 저장하는 값을 불러오는 버튼입니다.

System문구는 버튼을 누른 후 메세지를 나타내줍니다.
게임이 시작되면 "Game Start!!!"
입력값이 틀렸을 경우 "Wrong position (x, y), input num"
값을 입력하지 않고 버튼을 누르면 "Please Input Value"
스도쿠를 완성하였을 경우 "Congratulation! 'score', you awarded 'rank'!"가 표시됩니다.