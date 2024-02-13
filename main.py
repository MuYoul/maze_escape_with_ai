import streamlit as st
from maze_generator import generate_maze

# 미로의 크기 설정 (예시로 10x10을 사용)
width, height = 10, 10

# 미로를 시각적으로 표시하는 함수 수정
def display_maze(vertical_walls, horizontal_walls):
    maze_html = "<style>td{width: 24px; height: 24px;} .wall{background-color: black;} .space{background-color: white;}</style>"
    maze_html += "<table>"
    for y in range(height):
        maze_html += "<tr>"
        for x in range(width):
            if x < width - 1:
                maze_html += '<td class="space"></td>' if not vertical_walls[y][x] else '<td class="wall"></td>'
            else:
                maze_html += '<td class="space"></td>'
        maze_html += "</tr>"
        if y < height - 1:
            maze_html += "<tr>"
            for x in range(width):
                maze_html += '<td class="space"></td>' if not horizontal_walls[y][x] else '<td class="wall"></td>'
            maze_html += "</tr>"
    maze_html += "</table>"

    return maze_html

# Streamlit 앱 설정
st.title("미로 찾기 게임")

# 미로 생성 및 시각적으로 표시
vertical_walls, horizontal_walls = generate_maze(width, height)
st.markdown(display_maze(vertical_walls, horizontal_walls), unsafe_allow_html=True)

# 각 요소 설명 추가
st.write("🟩 - 공간: 미로를 탐색할 수 있는 경로")
st.write("⬛ - 벽: 미로에서 이동할 수 없는 부분")
