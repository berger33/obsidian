---
id: software.seguranca.tranche03.000226
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

# Tracee Captura Forense Automática (`--capture` / `output.artifacts`): coleta de binários executados, dumps de memória, arquivos e `PCAP`

## Em uma frase
Conforme destacado na seção *Forensic Capabilities* da visão geral oficial (`docs/docs/overview.md`), o Tracee vai além de emitir alertas: ele possui um motor de **Captura Forense (`--capture` / `artifacts`)** que extrai e salva automaticamente em disco os artefatos reais envolvidos no incidente no exato momento da execução!

## Por que importa
Se um atacante executar um binário de exploit em memória ou um binário temporário que se auto-deleta em 50 milissegundos (`rm -f /tmp/exploit`), quando o analista do SOC abrir o alerta 5 minutos depois o arquivo não existirá mais no container.

## Como funciona
Habilitando as opções de captura do Tracee (**`--capture exec`** para salvar uma cópia de todo binário executado, **`--capture mem`** para salvar dumps de regiões de memória onde ocorreu `unpacking`/W^X, **`--capture file-write`** para arquivos gravados, **`--capture module`** para módulos de kernel carregados e **`--capture net`** para arquivos `.pcap` por container/processo/comando), o Tracee preserva a evidência forense diretamente a partir das estruturas do kernel!

## Exemplo
```bash
# Iniciando o Tracee com captura forense automática de binários executados, regiões de memória suspeitas e tráfego DNS/HTTP em PCAP:
tracee \
  --policy ./runtime-advanced-threat-detection.yaml \
  --capture dir:/var/tracee/out \
  --capture exec \
  --capture mem \
  --capture net=per-container
```

## Limites e trade-offs
Para evitar gravar cópias repetidas de binários idênticos, o Tracee deduplica automaticamente os executáveis capturados pelo seu hash no diretório de saída (`/var/tracee/out/<host_or_container_id>/`).

## Como verificar
Inspecione os artefatos salvos em `/var/tracee/out/` após simular a execução de um binário em um container de teste.

## Conexões
- [[tracee-built-in-security-events-signatures-fileless-rootkit-escape]] — Veja também: Tracee Assinaturas de Segurança Embutidas: detecção de execução *Fileless* (`mem_prot_alert`), *Rootkits* (` hooked_syscall`), `anti_debugging` e Escape.
- [[tracee-eventos-rede-ebpf-dns-http-net-packet-flow-visibilidade]] — Veja também: Tracee Visibilidade de Rede via eBPF (`net_packet_dns`, `net_packet_http`, `net_flow_tcp_begin`): inspeção sem proxy ou sidecar.

## Fontes
- [Aqua Security Tracee Official Documentation — Overview (Everything is an Event Architecture, 400+ Syscalls, Built-in Signatures, Forensic Capture & Security Model)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md) — Visão geral oficial da documentação do Tracee detalhando o pipeline unificado de eventos, assinaturas de detecção embutidas, coleta forense e modelo de ameaças; consultado em 2026-10-03.
- [Aqua Security Tracee Official Documentation — Policies Reference (Kubernetes CRD v1beta1 vs Plain Format, 64 Policies, Scopes & Event Filters)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md) — Referência oficial de políticas do Tracee explicando a intercambiabilidade entre o formato CRD Kubernetes e Plain YAML, escopos e filtros; consultado em 2026-10-03.
- [Aqua Security Tracee — Official GitHub Repository](https://github.com/aquasecurity/tracee) — Repositório oficial Apache-2.0 do Aqua Security Tracee; consultado em 2026-10-03.
