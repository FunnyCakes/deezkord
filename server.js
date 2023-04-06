const { spawn } = require("child_process");

const startBot = () => {
  const bot = spawn("python", ["index.py"]);

  bot.stdout.on("data", (data) => {
    console.log(`stdout: ${data}`);
  });

  bot.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
  });

  bot.on("close", (code) => {
    console.log(`Bot exited with code ${code}`);
    startBot();
  });
};

startBot();
