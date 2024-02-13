import random

def create_maze(width, height, start, end):
  """
  직사각형 미로 생성 함수

  Args:
    width: 미로 너비
    height: 미로 높이
    start: 시작 위치 (x, y) 튜플
    end: 끝 위치 (x, y) 튜플

  Returns:
    2차원 리스트 (미로)
  """

  # 2D 배열 생성
  maze = [[' ' for _ in range(width)] for _ in range(height)]

  # 시작 위치 및 끝 위치 설정
  x, y = start
  goal_x, goal_y = end

  # 재귀 함수 정의
  def dfs(x, y, goal):
    # 현재 위치 방문 표시
    maze[y][x] = 'o'

    # 이동 가능한 방향 목록
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # 무작위로 방향 선택
    random.shuffle(directions)

    for dx, dy in directions:
      # 이동하려는 위치가 범위 내에 있고 방문하지 않았다면
      if 0 <= x + dx < width and 0 <= y + dy < height and maze[y + dy][x + dx] == ' ':
        # 벽 제거
        maze[y][x + dx // 2] = '.'
        maze[y + dy // 2][x] = '.'

        # 다음 위치 탐색
        if (x + dx, y + dy) != goal:
          dfs(x + dx, y + dy, goal)

  # 재귀 함수 시작
  dfs(x, y, (goal_x, goal_y))

  return maze

def print_maze(maze):
  """
  미로 출력 함수

  Args:
    maze: 2차원 리스트 (미로)
  """
  for row in maze:
    print(''.join(row))

# 미로 크기 설정
width = 10
height = 10

# 시작 위치 설정
start_x = 0
start_y = 0

# 끝 위치 설정
end_x = 9
end_y = 9

# 미로 생성 및 출력
maze = create_maze(width, height, (start_x, start_y), (end_x, end_y))
print_maze(maze)
