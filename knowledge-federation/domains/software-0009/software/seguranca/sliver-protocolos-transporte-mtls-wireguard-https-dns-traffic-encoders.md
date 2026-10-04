---
id: software.seguranca.tranche16.001543
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

# Engenharia dos 4 Canais de Transporte C2 do Sliver (**`mtls`**, **`wg` WireGuard**, **`https` C2 Profiles** e **`dns` Canário**) e **Traffic Encoders (Wasm)**

## Em uma frase
Quando você planeja um exercício de Purple Team para testar a visibilidade do SOC corporativo, quando deve escolher cada um dos 4 transportes do Sliver (**`mtls`**, **`wg`**, **`https`** ou **`dns`**)?

## Por que importa
Veja as características técnicas de cada transporte: **(1) `mtls` (*Mutual TLS*)** — é o transporte mais rápido e seguro quando conexões TLS diretas são permitidas no firewall, pois exige **autenticação mútua de certificado X.509** no próprio handshake TLS (qualquer scanner da internet ou analista de Blue Team que tentar conectar na porta sem o certificado cliente do implante é rejeitado imediatamente na camada TLS!).

## Como funciona
**(2) `wg` (*WireGuard*)** — estabelece um túnel UDP criptografado `Noise_IK` na memória do implante (sem precisar criar interface de kernel no alvo!) e faz rotação automática de chaves; **(3) `http`/`https`** — ideal para atravessar **Proxies Corporativos com Inspeção TLS (*SSL Inspection*)**, usando **HTTP C2 Profiles** e **Traffic Encoders (compilados em WebAssembly `.wasm`)** para disfarçar os payloads como tráfego web normal; e **(4) `dns`** — canal lento mas resiliente para redes sem saída direta à internet!

## Exemplo
```text
# Iniciar um listener WireGuard C2 (UDP 51820) e listar os Traffic Encoders WebAssembly disponiveis no Sliver
sliver > wg --lport 51820
sliver > traffic-encoders
sliver > jobs
```

## Limites e trade-offs
Por que o transporte **`http`/`https`** do Sliver é o único que funciona quando a empresa possui um **Proxy Web Corporativo com TLS Interception (MITM Proxy)**? Porque um proxy corporativo com inspeção SSL substitui o certificado do servidor pelo certificado da CA interna da empresa — o que **quebra intencionalmente a verificação de certificado fixado do `mtls`**, mas passa normalmente pelo transporte `https` do Sliver passando pelo proxy do sistema operacional!

## Como verificar
Ao configurar um listener `dns` no Sliver (`dns --domains c2-dns.exemplo.br`), você também pode ativar **Canary Domains** para detectar se um sandbox ou analista de segurança está tentando resolver domínios internos do implante.

## Conexões
- [[sliver-modos-operacao-beacon-assincrono-jitter-vs-session-interativa]] — Veja também: Implantes Sliver: **Beacon Mode (Assíncrono com Intervalo + Jitter)** vs. **Session Mode (Tempo Real)** e Promoção On-Demand com **`interactive`**.
- [[sliver-modo-multiplayer-operadores-grpc-mtls-rbac-auditoria-logs]] — Veja também: Operação em Equipe (**Multiplayer Mode** sobre gRPC mTLS), Gerenciamento de Operadores (**`new-operator`**) e **Audit Log JSON** Completo para Purple Team no Sliver.
- [[sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns]] — Referência cruzada direta com sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns.

## Fontes
- [Sliver Adversary Emulation Framework Official Repository (`BishopFox/sliver`)](https://raw.githubusercontent.com/BishopFox/sliver/master/README.md) — repositório oficial do framework C2 Sliver em Go cobrindo implantes multi-plataforma, chaves assimétricas únicas por binário e execução BOF/COFF; consultado em 2026-10-03.
- [Sliver Official Documentation — Getting Started (`sliver.sh/docs?name=Getting+Started`)](https://sliver.sh/docs?name=Getting+Started) — documentação oficial do Sliver detalhando arquitetura Server/Multiplayer, diferença entre `Beacon Mode` e `Session Mode`, geração de implantes, `interactive` e Stagers; consultado em 2026-10-03.
