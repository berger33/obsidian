---
id: software.seguranca.tranche14.001357
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/arkime/arkime/main/README.md", "https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Segurança e Autenticação do **Arkime Viewer**: `passwordSecret`, `serverSecret`, TLS Mútuo entre Sensores e Integração **SSO (`authMode=header-jwt` / OIDC)**

## Em uma frase
Como os sensores Arkime armazenam o tráfego bruto de toda a rede da empresa, comprometer o **Arkime Viewer (`:8005`)** daria a um atacante acesso a pacotes internos sensíveis. Quais são os controles de segurança obrigatórios documentados pela equipe do Arkime para blindar os sensores e o Viewer?

## Por que importa
Primeiro: configure **`passwordSecret`** e **`serverSecret`** na seção `[default]` do `/opt/arkime/etc/config.ini` com strings aleatórias longas e distintas (e proteja o `config.ini` com `chmod 0600`)! O `passwordSecret` cifra os hashes de senha dos usuários antes de salvá-los no OpenSearch (impedindo que alguém com acesso direto ao OpenSearch injete uma conta administrativa forjada!), enquanto o `serverSecret` autentica criptograficamente a comunicação *Server-to-Server (S2S)* quando o `viewer` central solicita fatias de `.pcap` aos sensores remotos na porta `8005`!

## Como funciona
Segundo: habilite **TLS (`certFile` e `keyFile`)** em todos os processos `viewer`. E terceiro: integre o Viewer ao seu **SSO Corporativo (Authentik, Kanidm, Keycloak, Pomerium, AWS ALB OIDC)** usando **`authMode=header-jwt`** (ou `userNameHeader` + `requiredAuthHeader`) atrás de um Proxy Reverso autenticado!

## Exemplo
```ini
# Configuracao de seguranca no /opt/arkime/etc/config.ini com TLS nos sensores, segredos criptograficos S2S e autenticacao SSO JWT via Proxy
[default]
certFile=/opt/arkime/etc/arkime.cert
keyFile=/opt/arkime/etc/arkime.key
passwordSecret=SegredoCriptografiaHashesMuitoLongoAleatorio2026
serverSecret=SegredoComunicacaoInterSensoresS2SAleatorio2026
viewHost=127.0.0.1
viewPort=8005
authMode=header-jwt
userNameHeader=x-forwarded-jwt
authUserIdField=preferred_username
```

## Limites e trade-offs
Atenção máxima ao usar **`userNameHeader`** ou **`authMode=header-jwt`**: como o `viewer` confia que o Proxy Reverso (Nginx/Envoy/ALB) à sua frente já validou a assinatura do JWT OIDC, você **DEVE configurar `viewHost=127.0.0.1`** (ou bloquear a porta `8005` no `nftables` para aceitar apenas os IPs do Proxy Reverso e dos outros sensores Arkime)!

## Como verificar
Utilize também o controle de acesso baseado em papéis (**Roles** no Arkime, como `arkimeUser`, `parliamentUser`, `cont3xtUser`) e **Forced Expressions** por usuário/papel (por exemplo, restringindo um administrador de uma filial para enxergar apenas sessões com `ip == 10.50.0.0/16` e ocultando pacotes de redes restritas!).

## Conexões
- [[arkime-ecossistema-parliament-cont3xt-esproxy-federacao-multi-cluster]] — Veja também: O Ecossistema Completo do Arkime: **`Parliament`** (Multi-Cluster Dashboard), **`Cont3xt`** (Agregador de CTI/OSINT) e **`esProxy`**.
- [[arkime-ingestao-pcap-offline-dfir-capture-r-analise-forense]] — Veja também: Uso do Arkime em **Laboratórios de DFIR Offline (`capture -r`)**: Importando Diretórios de Arquivos `.pcap` de Incidentes para Investigação Visual e Grafo.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.
- [[authentik-outposts-proxy-forwardauth-ldap-radius-arquitetura-distribuida]] — Referência cruzada direta com authentik-outposts-proxy-forwardauth-ldap-radius-arquitetura-distribuida.

## Fontes
- [Arkime Official GitHub Repository (`arkime/arkime`)](https://raw.githubusercontent.com/arkime/arkime/main/README.md) — repositório oficial do sistema de Full Packet Capture Arkime cobrindo arquitetura distribuída `capture` (C), `viewer` (Node.js), OpenSearch/Elasticsearch, `wiseService`, `Parliament` e `Cont3xt`; consultado em 2026-10-03.
- [Arkime Official Sample Configuration (`release/config.ini.sample`)](https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample) — referência oficial do `/opt/arkime/etc/config.ini` cobrindo herança em camadas, `pcapDir`, `freeSpaceG`, `pcapReadMethod=tpacketv3`, criptografia AES-256-CTR em repouso, `passwordSecret`, `serverSecret` e `authMode=header-jwt`; consultado em 2026-10-03.
