---
id: software.seguranca.tranche03.000227
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md", "https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md", "https://github.com/aquasecurity/tracee"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Tracee Visibilidade de Rede via eBPF (`net_packet_dns`, `net_packet_http`, `net_flow_tcp_begin`): inspeção sem proxy ou sidecar

## Em uma frase
Conforme documentado em `docs/docs/overview.md` (*Network events including DNS, HTTP, and packet analysis*), o Tracee captura e decodifica tráfego de rede diretamente nos hooks `cgroup_skb` / TC do eBPF, expondo eventos estruturados de **DNS (`net_packet_dns_request`, `net_packet_dns_response`)**, **HTTP (`net_packet_http_request`, `net_packet_http_response`)** e **Fluxos TCP (`net_flow_tcp_begin`, `net_flow_tcp_end`)** já enriquecidos com o PID, o binário executável e o Pod Kubernetes exatos que geraram o pacote!

## Por que importa
Em um sensor de rede externo (ou mesmo em logs de VPC Flow Logs), você vê que o IP do nó worker fez uma consulta DNS para um domínio malicioso, mas não sabe qual dos 80 containers nem qual processo específico dentro do container realizou aquela chamada.

## Como funciona
No Tracee, todo evento de rede carrega o contexto completo do processo (`processName`, `pid`, `hostPid`, `containerId`, `k8s.podName`, `k8s.namespace`), unificando telemetria de host e rede em um único evento JSON.

## Exemplo
```yaml
type: policy
name: monitor-container-dns-and-http
description: Registra consultas DNS e requisições HTTP de saída com o processo e container responsáveis
scope:
  - container
rules:
  - event: net_packet_dns_request
  - event: net_packet_http_request
```

## Limites e trade-offs
Combine eventos de rede (`net_packet_dns_request`) com eventos de processo (`sched_process_exec`) na mesma política para reconstruir toda a cadeia de *Kill Chain* de um ataque (exploit HTTP -> spawn de shell -> resolução DNS -> download de payload).

## Como verificar
Ative a política acima e execute `curl -I http://example.com` dentro de um container para inspecionar os eventos JSON gerados.

## Conexões
- [[tracee-forensic-capture-artifacts-executables-memory-pcap-files]] — Veja também: Tracee Captura Forense Automática (`--capture` / `output.artifacts`): coleta de binários executados, dumps de memória, arquivos e `PCAP`.
- [[tracee-assinaturas-customizadas-golang-cel-extensibilidade-deteccao]] — Veja também: Tracee Criação de Assinaturas Customizadas: escrita de detectores próprios consumindo o pipeline de eventos do Tracee.

## Fontes
- [Aqua Security Tracee Official Documentation — Overview (Everything is an Event Architecture, 400+ Syscalls, Built-in Signatures, Forensic Capture & Security Model)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md) — Visão geral oficial da documentação do Tracee detalhando o pipeline unificado de eventos, assinaturas de detecção embutidas, coleta forense e modelo de ameaças; consultado em 2026-10-03.
- [Aqua Security Tracee Official Documentation — Policies Reference (Kubernetes CRD v1beta1 vs Plain Format, 64 Policies, Scopes & Event Filters)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md) — Referência oficial de políticas do Tracee explicando a intercambiabilidade entre o formato CRD Kubernetes e Plain YAML, escopos e filtros; consultado em 2026-10-03.
- [Aqua Security Tracee — Official GitHub Repository](https://github.com/aquasecurity/tracee) — Repositório oficial Apache-2.0 do Aqua Security Tracee; consultado em 2026-10-03.
