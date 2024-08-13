import { useState } from "react";

function Counter({ initialCount }) {
  const [count, setCount] = useState(initialCount);

  const increment = () => {
    console.log("increment", "count=", count);
    // setCount(count + 1);
    // setCount(count + 1);
    setCount(prevCount => prevCount + 1);
    setCount(prevCount => prevCount + 1);
  };
  const decrement = () => {
    setCount(prevCount => prevCount - 1);
  };
  return (
    <button
      onClick={() => increment()}
      onContextMenu={e => {
        e.preventDefault();
        decrement();
      }}
    >
      {count}
    </button>
  );
}

function App() {
  const style = { margin: "1em" };

  return (
    <div className={"App"} style={style}>
      <Counter initialCount={10} />
      <Counter initialCount={12} />
      <Counter initialCount={13} />
    </div>
  );
}

export default App;
