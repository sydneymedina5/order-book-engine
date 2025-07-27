import React, { useEffect, useState, useRef } from 'react';
import { View, Text, FlatList, StyleSheet, SafeAreaView } from 'react-native';

const WEBSOCKET_URL = 'ws://<YOUR_IP>:8000/ws/orderbook'; // Replace <YOUR_IP>

const OrderBook = () => {
  const [orderBook, setOrderBook] = useState({ bids: [], asks: [] });
  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket(WEBSOCKET_URL);

    ws.current.onopen = () => {
      console.log('Connected to WebSocket');
    };

    ws.current.onmessage = (e) => {
      const data = JSON.parse(e.data);
      setOrderBook(data);
    };

    ws.current.onerror = (e) => {
      console.error('WebSocket error', e.message);
    };

    ws.current.onclose = () => {
      console.log('WebSocket closed');
    };

    return () => {
      ws.current.close();
    };
  }, []);

  const renderItem = ({ item }) => (
    <View style={styles.row}>
      <Text style={styles.cell}>{item[0]}</Text>
      <Text style={styles.cell}>{item[1]}</Text>
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>Order Book</Text>

      <Text style={styles.subheading}>Asks</Text>
      <FlatList
        data={orderBook.asks}
        renderItem={renderItem}
        keyExtractor={(_, index) => `ask-${index}`}
      />

      <Text style={styles.subheading}>Bids</Text>
      <FlatList
        data={orderBook.bids}
        renderItem={renderItem}
        keyExtractor={(_, index) => `bid-${index}`}
      />
    </SafeAreaView>
  );
};

export default OrderBook;

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 10 },
  subheading: { fontSize: 18, marginTop: 20 },
  row: { flexDirection: 'row', justifyContent: 'space-between', paddingVertical: 5 },
  cell: { fontSize: 16 }
});
