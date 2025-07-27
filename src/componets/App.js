import React, { useEffect, useState, useRef } from 'react';
import { Text, View, FlatList, StyleSheet } from 'react-native';

const socketURL = "ws://192.168.1.42:8080/ws/orderbook";  // <-- your machine IP here

export default function App() {
  const [orderBook, setOrderBook] = useState({ bids: [], asks: [] });
  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket(socketURL);

    ws.current.onopen = () => {
      console.log("WebSocket connected");
    };

    ws.current.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setOrderBook(data);
    };

    ws.current.onerror = (e) => {
      console.log("WebSocket error", e.message);
    };

    ws.current.onclose = () => {
      console.log("WebSocket closed");
    };

    return () => {
      ws.current.close();
    };
  }, []);

  const renderItem = ({ item }) => (
    <View style={styles.row}>
      <Text>{item[0]}</Text>
      <Text>{item[1]}</Text>
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Order Book</Text>

      <Text style={styles.heading}>Asks</Text>
      <FlatList data={orderBook.asks} renderItem={renderItem} keyExtractor={(_, i) => `ask-${i}`} />

      <Text style={styles.heading}>Bids</Text>
      <FlatList data={orderBook.bids} renderItem={renderItem} keyExtractor={(_, i) => `bid-${i}`} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, marginTop: 40, padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold' },
  heading: { marginTop: 20, fontSize: 18, fontWeight: '600' },
  row: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 8 },
});
