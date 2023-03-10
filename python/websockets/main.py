import asyncio
import ssl
import json
from datetime import datetime

import certifi
import websockets
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())


class CoinGraph:
    def __init__(self, coin: str):
        self.coin = coin
        self._ax = None
        self._fig = plt.figure()
        self._xdata, self._ydata = [], []

    def _init_graph(self):
        self._ax = self._fig.add_subplot(111)
        self._fig.show()

    def _update_graph(self):
        self._ax.plot(self._xdata, self._ydata, color='g')
        self._ax.legend([f'Last price: {self._ydata[-1]}$'])
        self._fig.canvas.draw()
        plt.pause(0.3)

    async def show(self):
        self._init_graph()
        url = f'wss://stream.binance.com:443/stream?streams={self.coin}@miniTicker'
        async with websockets.connect(url, ssl=ssl_context) as client:
            while True:
                data = json.loads(await client.recv())['data']
                epoch_time = data['E'] // 1000
                event_time = datetime.fromtimestamp(epoch_time).strftime('%H:%M:%S')
                event_price = int(float(data['c']))

                self._xdata.append(event_time)
                self._ydata.append(event_price)

                self._update_graph()


def main():
    bitcoin_graph = CoinGraph('btcusdt')
    asyncio.run(bitcoin_graph.show())


if __name__ == '__main__':
    main()
