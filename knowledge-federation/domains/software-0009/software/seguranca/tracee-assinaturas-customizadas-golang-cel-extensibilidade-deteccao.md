---
id: software.seguranca.tranche03.000228
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

# Tracee Criação de Assinaturas Customizadas: escrita de detectores próprios consumindo o pipeline de eventos do Tracee

## Em uma frase
Conforme enfatiza a seção *Unified Architecture* de `docs/docs/overview.md` (*"Custom signatures integrate naturally with built-in events"*), o motor de detecção do Tracee permite que equipes de Detection Engineering criem **assinaturas customizadas** em Go (implementando a interface `detect.Signature`) que se inscrevem em um ou mais eventos do Tracee (syscalls, hooks LSM ou eventos de rede) e emitem novos eventos de detecção de alto nível.

## Por que importa
Às vezes uma simples regra de filtro sobre um único evento não basta porque a detecção exige manter estado entre múltiplos eventos (por exemplo: um processo que primeiro lê `/var/run/secrets/kubernetes.io/serviceaccount/token` e, nos 30 segundos seguintes, abre uma conexão de rede para um IP externo fora do cluster).

## Como funciona
Uma assinatura do Tracee declara na função `GetSelectedEvents()` apenas os eventos de entrada de que precisa; o motor eBPF do Tracee ativa automaticamente apenas esses coletores no kernel e entrega os eventos para o método `OnEvent(event protocol.Event)` da sua assinatura!

## Exemplo
```go
// Estrutura essencial de uma assinatura customizada em Go para o motor de detecção do Tracee:
func (sig *MyCustomDetector) GetSelectedEvents() ([]detect.SignatureEventSelector, error) {
    return []detect.SignatureEventSelector{
        {Source: "tracee", Name: "security_file_open"},
        {Source: "tracee", Name: "security_socket_connect"},
    }, nil
}
```

## Limites e trade-offs
Como o Tracee resolve dependências de eventos automaticamente (*Event Dependency Resolution*), você nunca precisa habilitar manualmente no YAML os eventos de baixo nível que alimentam uma assinatura de alto nível: basta referenciar o nome da assinatura na seção `rules:` da política!

## Como verificar
Teste suas assinaturas customizadas passando o diretório de plugins/assinaturas para o binário do Tracee.

## Conexões
- [[tracee-eventos-rede-ebpf-dns-http-net-packet-flow-visibilidade]] — Veja também: Tracee Visibilidade de Rede via eBPF (`net_packet_dns`, `net_packet_http`, `net_flow_tcp_begin`): inspeção sem proxy ou sidecar.
- [[tracee-implantacao-kubernetes-helm-daemonset-postee-webhook-siem]] — Veja também: Tracee em Kubernetes: implantação via Helm DaemonSet, CRDs `Policy` (`tracee.aquasec.com/v1beta1`) e roteamento de saída (`json`, `webhook`, `forward`).

## Fontes
- [Aqua Security Tracee Official Documentation — Overview (Everything is an Event Architecture, 400+ Syscalls, Built-in Signatures, Forensic Capture & Security Model)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md) — Visão geral oficial da documentação do Tracee detalhando o pipeline unificado de eventos, assinaturas de detecção embutidas, coleta forense e modelo de ameaças; consultado em 2026-10-03.
- [Aqua Security Tracee Official Documentation — Policies Reference (Kubernetes CRD v1beta1 vs Plain Format, 64 Policies, Scopes & Event Filters)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md) — Referência oficial de políticas do Tracee explicando a intercambiabilidade entre o formato CRD Kubernetes e Plain YAML, escopos e filtros; consultado em 2026-10-03.
- [Aqua Security Tracee — Official GitHub Repository](https://github.com/aquasecurity/tracee) — Repositório oficial Apache-2.0 do Aqua Security Tracee; consultado em 2026-10-03.
