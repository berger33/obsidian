---
id: software.seguranca.tranche12.001173
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

# Handshake **1-RTT (`Noise_IKpsk2`)**, **Perfect Forward Secrecy (PFS)**, Rotação Automática de Chaves a Cada 2 Minutos e **`PresharedKey` Pós-Quântica**

## Em uma frase
Como o protocolo WireGuard estabelece uma sessão segura em apenas **1 Round-Trip Time (1-RTT)**, garante **Perfect Forward Secrecy (PFS)** contra gravação passiva de tráfego, evita ataques de *Key-Compromise Impersonation (KCI)* e protege os dados hoje contra futuros computadores quânticos (*Harvest Now, Decrypt Later*)?

## Por que importa
Quando o *Initiator* tem um pacote para enviar ao *Responder*, ele gera uma chave efêmera `Curve25519` nova e envia a ** Primeira Mensagem (`handshake_initiation`, 148 bytes)** — onde a própria chave pública estática do Initiator vai **criptografada** (*Identity Hiding*: um observador passivo na rede nem sequer descobre qual cliente está se conectando!) junto com um timestamp `TAI64N` de 12 bytes (que previne replay de pacotes de handshake). O *Responder* responde com a **Segunda Mensagem (`handshake_response`, 92 bytes)** contendo sua chave efêmera e derivando as chaves simétricas `ChaCha20-Poly1305` via `HKDF` sobre múltiplos cálculos ECDH (`es`, `ss`, `ee`, `se`)!

## Como funciona
Para garantir **Perfect Forward Secrecy contínua**, o WireGuard é um protocolo orientado a timers: **as chaves de sessão são renegociadas automaticamente a cada `REKEY_AFTER_TIME` (~120 segundos / 2 minutos)** ou após `REKEY_AFTER_MESSAGES` pacotes, e todas as chaves efêmeras e simétricas antigas são **zeradas da memória RAM do kernel após `REJECT_AFTER_TIME * 3` (~9 minutos)**!

## Exemplo
```bash
# Inspecionar com wg show o timestamp do ultimo handshake (latest handshake) que se renova automaticamente a cada ~2 minutos durante trafego ativo
sudo wg show wg0
sudo wg show wg0 latest-handshakes
```

## Limites e trade-offs
Por que você deve SEMPRE configurar a diretiva **`PresharedKey`** (`wg genpsk`) em cada bloco `[Peer]` de produção? Porque embora um futuro computador quântico suficientemente potente rodando o Algoritmo de Shor possa quebrar a criptografia assimétrica de curva elíptica (`Curve25519`), quando o `PresharedKey` (32 bytes / 256 bits de entropia simétrica pura) está configurado, o WireGuard mistura essa chave simétrica via `HKDF` na derivação das chaves de sessão — exigindo o Algoritmo de Grover sobre 256 bits (inviável quanticamente) e conferindo **resistência pós-quântica imediata** ao tráfego gravado!

## Como verificar
Se não houver tráfego fluindo no túnel, o WireGuard para de fazer handshakes e zera as chaves de sessão da RAM até que um novo pacote precise ser transmitido.

## Conexões
- [[wireguard-cryptokey-routing-allowedips-tabela-roteamento-peers]] — Veja também: O Conceito Central do WireGuard — **Cryptokey Routing (`AllowedIPs`)**: Unificando Tabela de Roteamento IP e Lista de Controle de Acesso Criptográfica.
- [[wireguard-furtividade-silencio-udp-cookie-reply-mitigacao-dos]] — Veja também: Furtividade de Rede (*Stealth*) e Mitigação de **DoS (`mac1`, `mac2` e `Cookie Reply`)** no WireGuard: Por Que o WireGuard é Invisível ao Nmap.
- [[wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia]] — Referência cruzada direta com wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia.

## Fontes
- [WireGuard Official Protocol & Cryptography Specification (`wireguard.com/protocol`)](https://www.wireguard.com/protocol/) — especificação criptográfica oficial do WireGuard detalhando as primitivas fixas (`Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s`), timers de PFS, `PresharedKey` e mitigação de DoS com `mac1`/`mac2` cookies; consultado em 2026-10-03.
- [WireGuard Official Quick Start & CLI Guide (`wireguard.com/quickstart`)](https://www.wireguard.com/quickstart/) — guia oficial de operação com `ip link`, `wg(8)`, `wg-quick(8)`, geração de chaves, `PersistentKeepalive` para travessia de NAT e `dynamic_debug` no kernel Linux; consultado em 2026-10-03.
