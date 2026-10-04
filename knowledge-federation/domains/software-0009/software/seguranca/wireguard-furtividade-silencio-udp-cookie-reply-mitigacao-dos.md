---
id: software.seguranca.tranche12.001174
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://www.wireguard.com/protocol/", "https://www.wireguard.com/quickstart/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Furtividade de Rede (*Stealth*) e Mitigação de **DoS (`mac1`, `mac2` e `Cookie Reply`)** no WireGuard: Por Que o WireGuard é Invisível ao Nmap

## Em uma frase
Se um atacante na internet rodar um scan **`nmap -sU -p 51820`** contra o endereço IP público do seu servidor WireGuard, o que o servidor WireGuard responde? **Absolutamente nada (0 pacotes enviados de volta)**!

## Por que importa
Ao contrário do OpenVPN, IPsec ou SSH (onde qualquer scanner na internet descobre imediatamente que a porta está aberta porque o servidor responde ao handshake inicial), **um servidor WireGuard é 100% silencioso para qualquer cliente que não conheça previamente a Chave Pública estática do servidor E não esteja listado como um `[Peer]` autorizado pelo servidor**!

## Como funciona
Isso é implementado no protocolo através dos campos **`mac1` e `mac2` (`BLAKE2s` keyed MACs)** no final de toda mensagem de handshake: **(1)** Todo pacote de handshake deve terminar com um `mac1` de 16 bytes calculado usando o hash da chave pública do receptor (`LABEL_MAC1` + `pubkey`); se o `mac1` for inválido, o pacote é descartado silenciosamente em microssegundos sem fazer nenhuma multiplicação `Curve25519`! **(2)** Se o servidor estiver sob ataque de inundação de CPU (*DoS / Flood*) por alguém que conhece a chave pública do servidor, o servidor ativa o mecanismo **`Cookie Reply` (`XChaCha20-Poly1305`)**, exigindo que o iniciador prove posse do seu endereço IP de origem preenchendo o campo `mac2` (usando um segredo que muda a cada 2 minutos) antes de o servidor realizar qualquer operação cara de curva elíptica!

## Exemplo
```bash
# Verificar estatisticas de pacotes e bytes transferidos por peer na interface wg0 sem expor chaves privadas
sudo wg show wg0 transfer
sudo wg show wg0 endpoints
```

## Limites e trade-offs
Essa combinação de **`mac1` (invisibilidade a scanners)** + **`mac2` / `Cookie Reply` (proteção anti-DoS sem alocação de estado em memória)** permite expor a porta UDP do WireGuard na internet com uma superfície de ataque pré-autenticação drasticamente menor que qualquer daemon TLS/IKE em userland!

## Como verificar
Quando um cliente está atrás de um roteador NAT ou firewall stateful e precisa receber conexões iniciadas pelo servidor mesmo após longos períodos de silêncio, configure **`PersistentKeepalive = 25`** no bloco `[Peer]` do cliente para manter o mapeamento UDP aberto no NAT.

## Conexões
- [[wireguard-handshake-1rtt-pfs-rekeying-timers-presharedkey-pos-quantico]] — Veja também: Handshake **1-RTT (`Noise_IKpsk2`)**, **Perfect Forward Secrecy (PFS)**, Rotação Automática de Chaves a Cada 2 Minutos e **`PresharedKey` Pós-Quântica**.
- [[wireguard-operacao-cli-wg-wg-quick-iproute2-fwmark-roteamento]] — Veja também: Operação e Automação com **`wg(8)`**, **`wg-quick(8)`**, **`iproute2`** e Roteamento Baseado em Políticas (**`FwMark`** para Full-Tunnel sem Loop).
- [[wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia]] — Referência cruzada direta com wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia.

## Fontes
- [WireGuard Official Protocol & Cryptography Specification (`wireguard.com/protocol`)](https://www.wireguard.com/protocol/) — especificação criptográfica oficial do WireGuard detalhando as primitivas fixas (`Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s`), timers de PFS, `PresharedKey` e mitigação de DoS com `mac1`/`mac2` cookies; consultado em 2026-10-03.
- [WireGuard Official Quick Start & CLI Guide (`wireguard.com/quickstart`)](https://www.wireguard.com/quickstart/) — guia oficial de operação com `ip link`, `wg(8)`, `wg-quick(8)`, geração de chaves, `PersistentKeepalive` para travessia de NAT e `dynamic_debug` no kernel Linux; consultado em 2026-10-03.
