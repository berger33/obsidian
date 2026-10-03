---
id: software.seguranca.tranche03.000229
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
fontes: ["https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md", "https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md", "https://github.com/aquasecurity/tracee"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Tracee em Kubernetes: implantação via Helm DaemonSet, CRDs `Policy` (`tracee.aquasec.com/v1beta1`) e roteamento de saída (`json`, `webhook`, `forward`)

## Em uma frase
No Kubernetes, o Tracee é implantado como um **DaemonSet** (tipicamente no namespace `tracee-system` via Helm chart oficial `aqua/tracee`), monitorando automaticamente os recursos Kubernetes **`Policy` (`tracee.aquasec.com/v1beta1`)** no cluster e enriquecendo todos os eventos com metadados do runtime de container (`containerd`, `CRI-O`, `Docker`) e do Kubernetes (`podName`, `namespace`, `uid`).

## Por que importa
Gerenciar arquivos de configuração manualmente em cada nó de um cluster autoescalável (Karpenter / Cluster Autoscaler) não escala; com o operador/controlador de CRDs embutido no Tracee, aplicar `kubectl apply -f policy.yaml` atualiza as políticas em todos os nós do DaemonSet dinamicamente.

## Como funciona
Para exportar as detecções, o Tracee suporta múltiplos destinos em `--output`: **`json`**, **`table`**, **`gotemplate=`**, **`webhook:http://...`** (integrando-se a sistemas SOAR, Alertmanager, Falcosidekick ou Aqua Postee) e **`forward:tcp://...`** (protocolo Fluent Bit / Fluentd Forward).

## Exemplo
```bash
# Instalando o Tracee no cluster Kubernetes via Helm Chart oficial e verificando os CRDs de Policy:
helm repo add aqua https://aquasecurity.github.io/helm-charts/
helm repo update
helm install tracee aqua/tracee --namespace tracee-system --create-namespace
kubectl get policies.tracee.aquasec.com -A
```

## Limites e trade-offs
Ao enviar eventos para um SIEM ou webhook externo, utilize políticas focadas nas assinaturas de segurança e nos eventos filtrados de alta severidade, evitando enviar `sched_process_exec` global sem filtro para um endpoint HTTP síncrono.

## Como verificar
Verifique os logs do DaemonSet com `kubectl logs -n tracee-system -l app.kubernetes.io/name=tracee`.

## Conexões
- [[tracee-assinaturas-customizadas-golang-cel-extensibilidade-deteccao]] — Veja também: Tracee Criação de Assinaturas Customizadas: escrita de detectores próprios consumindo o pipeline de eventos do Tracee.
- [[tracee-modelo-seguranca-adversario-userspace-vs-kernel-garantias]] — Veja também: Tracee Modelo de Ameaças e Segurança (*Security Model*): resistência contra adversários em *userspace* e detecção de ameaças em *kernel*.

## Fontes
- [Aqua Security Tracee Official Documentation — Overview (Everything is an Event Architecture, 400+ Syscalls, Built-in Signatures, Forensic Capture & Security Model)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md) — Visão geral oficial da documentação do Tracee detalhando o pipeline unificado de eventos, assinaturas de detecção embutidas, coleta forense e modelo de ameaças; consultado em 2026-10-03.
- [Aqua Security Tracee Official Documentation — Policies Reference (Kubernetes CRD v1beta1 vs Plain Format, 64 Policies, Scopes & Event Filters)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md) — Referência oficial de políticas do Tracee explicando a intercambiabilidade entre o formato CRD Kubernetes e Plain YAML, escopos e filtros; consultado em 2026-10-03.
- [Aqua Security Tracee — Official GitHub Repository](https://github.com/aquasecurity/tracee) — Repositório oficial Apache-2.0 do Aqua Security Tracee; consultado em 2026-10-03.
