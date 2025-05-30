// スタイルを定義
const style = document.createElement("style");
style.textContent = `
  canvas {
    border: 2px solid #000;
    display: block;
    margin: 20px auto;
  }
  #message {
    text-align: center;
    font-size: 1.2em;
    margin-top: 10px;
  }
`;
document.head.appendChild(style);

// キャンバスを作成
const canvas = document.createElement("canvas");
canvas.id = "gameCanvas";
canvas.width = 300;
canvas.height = 300;
document.body.appendChild(canvas);

// メッセージ表示用のdivを作成
const message = document.createElement("div");
message.id = "message";
document.body.appendChild(message);

// ゲームロジック
const ctx = canvas.getContext("2d");
const CELL_SIZE = 100;
const BOARD_SIZE = 3;
let board = Array.from({ length: BOARD_SIZE }, () =>
  Array(BOARD_SIZE).fill(null)
);
let currentPlayer = "X";
let gameOver = false;

// グリッドを描画
function drawGrid() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.lineWidth = 2;

  for (let i = 1; i < BOARD_SIZE; i++) {
    // 縦線
    ctx.beginPath();
    ctx.moveTo(i * CELL_SIZE, 0);
    ctx.lineTo(i * CELL_SIZE, canvas.height);
    ctx.stroke();

    // 横線
    ctx.beginPath();
    ctx.moveTo(0, i * CELL_SIZE);
    ctx.lineTo(canvas.width, i * CELL_SIZE);
    ctx.stroke();
  }
}

// マークを描画
function drawMarks() {
  for (let row = 0; row < BOARD_SIZE; row++) {
    for (let col = 0; col < BOARD_SIZE; col++) {
      const mark = board[row][col];
      if (mark) {
        const x = col * CELL_SIZE + CELL_SIZE / 2;
        const y = row * CELL_SIZE + CELL_SIZE / 2;
        ctx.font = "48px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(mark, x, y);
      }
    }
  }
}

// 勝敗をチェック
function checkWinner() {
  // 行と列
  for (let i = 0; i < BOARD_SIZE; i++) {
    if (
      board[i][0] &&
      board[i][0] === board[i][1] &&
      board[i][1] === board[i][2]
    ) {
      return board[i][0];
    }
    if (
      board[0][i] &&
      board[0][i] === board[1][i] &&
      board[1][i] === board[2][i]
    ) {
      return board[0][i];
    }
  }

  // 斜め
  if (
    board[0][0] &&
    board[0][0] === board[1][1] &&
    board[1][1] === board[2][2]
  ) {
    return board[0][0];
  }
  if (
    board[0][2] &&
    board[0][2] === board[1][1] &&
    board[1][1] === board[2][0]
  ) {
    return board[0][2];
  }

  // 引き分け
  if (board.flat().every((cell) => cell)) {
    return "Draw";
  }

  return null;
}

// クリックイベント
canvas.addEventListener("click", (e) => {
  if (gameOver) return;

  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  const col = Math.floor(x / CELL_SIZE);
  const row = Math.floor(y / CELL_SIZE);

  if (board[row][col]) return;

  board[row][col] = currentPlayer;
  drawGrid();
  drawMarks();

  const winner = checkWinner();
  if (winner) {
    gameOver = true;
    message.textContent =
      winner === "Draw" ? "引き分けです！" : `${winner}の勝ちです！`;
  } else {
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    message.textContent = `${currentPlayer}の番です。`;
  }
});

// 初期描画
drawGrid();
message.textContent = `${currentPlayer}の番です。`;
