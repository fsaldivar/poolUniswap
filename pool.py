class LiquidityPool:
    def __init__(self, eth_amount, token_amount, fee_tier=0.01):
        self.eth_amount = eth_amount  # Cantidad inicial de ETH
        self.token_amount = token_amount  # Cantidad inicial de TOKEN
        self.k = eth_amount * token_amount  # Constante de producto
        self.fee_tier = fee_tier / 100  # Fee tier en porcentaje

    def swap_eth_for_token(self, eth_amount_in):
        # Paso 1: Imprimir las condiciones iniciales del pool
        print(f"1. Condiciones iniciales del pool:")
        print(f"ETH en el pool: x = {self.eth_amount} ETH")
        print(f"TOKEN en el pool: y = {self.token_amount} TOKEN")
        print(f"La ecuación de producto constante es: k = x * y = {self.eth_amount} * {self.token_amount} = {self.k}")
        print(f"Esta ecuación debe mantenerse constante después del intercambio.\n")

        # Paso 2: Cantidad de ETH a intercambiar y cálculo del fee
        print(f"2. Cantidad de ETH a intercambiar:")
        print(f"Vas a intercambiar {eth_amount_in} ETH.")
        fee = eth_amount_in * self.fee_tier
        print(f"Uniswap aplica una comisión (fee) del 0.01%, lo que significa que el fee es:")
        print(f"Fee = {eth_amount_in} * {self.fee_tier:.6f} = {fee:.6f} ETH")

        # Paso 3: Cálculo del ETH efectivo que realmente se añade al pool
        eth_amount_in_after_fee = eth_amount_in - fee
        print(f"Entonces, la cantidad de ETH efectiva que se intercambia (ETH que realmente se añade al pool) es:")
        print(f"ETH efectiva = {eth_amount_in} - {fee:.6f} = {eth_amount_in_after_fee:.6f} ETH\n")

        # Paso 4: Calcular el nuevo balance de ETH en el pool
        new_eth_balance = self.eth_amount + eth_amount_in_after_fee
        print(f"3. Nuevo balance de ETH en el pool:")
        print(f"ETH nuevo = {self.eth_amount} + {eth_amount_in_after_fee:.6f} = {new_eth_balance:.6f} ETH\n")

        # Paso 5: Calcular el nuevo balance de tokens en el pool usando la constante de producto
        print(f"4. Nuevo balance de TOKEN en el pool:")
        new_token_balance = self.k / new_eth_balance
        print(f"Usamos la constante de producto para calcular el nuevo balance de TOKEN:")
        print(f"y nuevo = k / x nuevo = {self.k} / {new_eth_balance:.6f} = {new_token_balance:.6f} TOKEN\n")

        # Paso 6: Tokens recibidos por el intercambio
        tokens_out = self.token_amount - new_token_balance
        print(f"5. Tokens recibidos:")
        print(f"Tokens recibidos = TOKEN inicial - TOKEN nuevo = {self.token_amount} - {new_token_balance:.6f} = {tokens_out:.6f} TOKEN\n")

        # Actualizamos los balances en el pool
        self.eth_amount = new_eth_balance
        self.token_amount = new_token_balance

        # Regresamos los valores calculados para mayor detalle
        return tokens_out, fee, self.eth_amount, self.token_amount


# Ejemplo de uso
pool = LiquidityPool(1, 100, fee_tier=0.01)  # 1 ETH = 100 TOKEN, 0.01% fee tier

# Supongamos que quieres intercambiar 0.1 ETH por TOKEN
eth_amount_in = 0.1
tokens_recibidos, fee, new_eth_balance, new_token_balance = pool.swap_eth_for_token(eth_amount_in)

# Print final para mostrar los resultados
print(f"6. Resumen final del intercambio:")
print(f"Tokens recibidos: {tokens_recibidos:.6f} TOKEN")
print(f"Fee cobrado: {fee:.6f} ETH")
print(f"Nuevo balance del pool -> ETH: {new_eth_balance:.6f}, TOKEN: {new_token_balance:.6f}")
