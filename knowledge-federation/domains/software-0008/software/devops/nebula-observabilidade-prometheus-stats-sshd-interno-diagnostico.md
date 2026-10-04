---
id: software.devops.tranche19.001890
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml", "https://raw.githubusercontent.com/slackhq/nebula/master/README.md", "https://github.com/slackhq/nebula"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nebula Observabilidade e Diagnóstico: exportação de métricas `stats` (Prometheus/Graphite) e servidor `sshd` interno de inspeção

## Em uma frase
O Nebula possui duas ferramentas nativas de observabilidade e troubleshooting em produção: a seção **`stats:`** (que exporta métricas detalhadas de handshakes, pacotes descartados pelo firewall, latência e bytes por túnel para **Prometheus** ou **Graphite**) e a seção **`sshd:`** (um servidor SSH administrativo embutido no processo Nebula para inspecionar o hostmap e túneis em memória).

## Por que importa
Quando dois nós não conseguem fechar túnel ou pacotes são descartados silenciosamente, reiniciar o daemon em modo debug corta as conexões ativas; já conectar no `sshd` administrativo interno permite rodar comandos como `list-hostmap`, `print-cert` e `query-lighthouse` em tempo real.

## Como funciona
Na seção `stats:`, basta configurar `type: prometheus`, `listen: 127.0.0.1:8080` e `path: /metrics` (com `message_metrics: true` e `lighthouse_metrics: true` opcionais) para coletar métricas de saúde da malha pelo Prometheus.

## Exemplo
```yaml
stats:
  type: prometheus
  listen: 127.0.0.1:8080
  path: /metrics
  namespace: nebula
  subsystem: overlay
  interval: 10s
  message_metrics: true
  lighthouse_metrics: true
```

## Limites e trade-offs
Se habilitar o servidor `sshd:` administrativo de diagnóstico em `config.yml`, faça bind estritamente em `127.0.0.1` (ou no IP Nebula do próprio nó) e restrinja `authorized_users` com chaves públicas SSH dedicadas.

## Como verificar
Consulte `curl -s http://127.0.0.1:8080/metrics | grep nebula_` para inspecionar os contadores de pacotes, handshakes e estado dos túneis.

## Conexões
- [[nebula-tuning-performance-listen-batch-routines-buffers-mtu]] — Veja também: Nebula Tuning de Alta Performance: ajuste de `routines`, `listen.batch`, buffers de socket (`read_buffer`/`write_buffer`) e MTU.

## Fontes
- [Nebula GitHub — README.md (Scalable Overlay Networking Tool, Noise Protocol ECDH/AES-256-GCM, nebula-cert PKI, Lighthouses & Curve P256/FIPS 140-3)](https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml) — README oficial do slackhq/nebula apresentando a arquitetura peer-to-peer autenticada por certificados, criação de CA/hosts e suporte a P256/FIPS; consultado em 2026-10-03.
- [Nebula Official Configuration Reference — examples/config.yml (PKI, Static Host Map, Lighthouse, Allow Lists, Listen Batch/Buffers, Punchy, Relay, TUN & Firewall)](https://raw.githubusercontent.com/slackhq/nebula/master/README.md) — Arquivo oficial comentado de referência config.yml do Nebula detalhando pki.blocklist, SIGHUP reload, static_host_map, lighthouse, punchy, relay, unsafe_routes e firewall; consultado em 2026-10-03.
- [Nebula — Official GitHub Repository](https://github.com/slackhq/nebula) — Repositório oficial MIT do Nebula; consultado em 2026-10-03.
