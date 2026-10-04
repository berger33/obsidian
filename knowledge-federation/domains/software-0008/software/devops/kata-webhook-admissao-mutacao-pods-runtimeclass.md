---
id: software.devops.tranche08.000708
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md", "https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md", "https://github.com/kata-containers/kata-containers"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kata Containers: mutating admission webhook (kata-webhook) para injeção transparente de RuntimeClass em Pods

## Em uma frase
O componente utilitário `Webhook` (`tools/testing/kata-webhook`) fornece um controlador de admissão mutante simples para anotar e configurar automaticamente Pods Kubernetes com a `runtimeClassName` do Kata Containers sem alterar manifestos existentes.

## Por que importa
Em grandes organizações ou pipelines de testes de conformidade (como testar charts Helm de terceiros sob isolamento Kata), editar manualmente centenas de manifestos de `Deployment`, `StatefulSet` e `Job` para adicionar o campo `spec.runtimeClassName: kata` é inviável. Conforme listado na tabela `Additional components` do README oficial do Kata Containers, o `kata-webhook` demonstra como automatizar essa transição na camada de admissão do Kubernetes.

## Como funciona
Implantado como um `MutatingAdmissionWebhook` no cluster Kubernetes, o `kata-webhook` intercepta requisições `CREATE` de objetos `Pod` no `kube-apiserver`. Caso o Pod pertença a um namespace monitorado (e não seja um Pod de rede `hostNetwork: true` incompatível com isolamento de VM), o webhook aplica um JSON Patch injetando automaticamente `spec.runtimeClassName` (por exemplo, `kata` ou `kata-qemu`) antes que o objeto seja persistido no `etcd` e agendado nos nós, permitindo rodar cargas de trabalho inteiras dentro de máquinas virtuais Kata de maneira 100% transparente para o desenvolvedor.

## Exemplo
```bash
# Verificar se um Pod criado sem runtimeClassName explícito no YAML recebeu a mutação do webhook para kata
kubectl get pod pod-teste-webhook -o jsonpath='{.spec.runtimeClassName}{"\n"}'
```

## Limites e trade-offs
Pods que exigem acesso direto ao namespace de rede do nó hospedeiro (`hostNetwork: true`), `hostPID: true` ou montagens privilegiadas de dispositivos físicos do host não podem ser isolados de forma transparente dentro de uma VM guest pelo webhook sem quebrar sua função; por isso, regras de mutação automática de `RuntimeClass` devem sempre excluir namespaces de sistema (`kube-system`) e DaemonSets de infraestrutura/CNI.

## Como verificar
Com o `kata-webhook` ativo em um namespace de homologação, crie um Pod simples (`kubectl run nginx --image=nginx`) e confirme via `kubectl get pod nginx -o yaml` que `runtimeClassName` foi preenchido automaticamente.

## Conexões
- [[kata-ferramentas-diagnostico-kata-ctl-agent-ctl-debug-trace]] — Veja também: Kata Containers: ferramentas de diagnóstico e depuração (kata-ctl, agent-ctl, kata-debug e trace-forwarder).
- [[kata-arquitetura-4-0-evolucao-rust-seguranca-confidencial]] — Veja também: Kata Containers: evolução para a Arquitetura 4.0, unificação em Rust e isolamento de workloads.
- [[kata-containers-isolamento-vms-leves-arquitetura]] — Referência cruzada direta com kata-containers-isolamento-vms-leves-arquitetura.
- [[kata-packaging-kata-deploy-helm-kubernetes-runtimeclass]] — Referência cruzada direta com kata-packaging-kata-deploy-helm-kubernetes-runtimeclass.
- [[kubescape-validating-admission-policies-cel-kubernetes]] — Referência cruzada direta com kubescape-validating-admission-policies-cel-kubernetes.

## Fontes
- [Kata Containers GitHub — README.md (Lightweight VMs, Hardware Requirements, Main & Additional Components)](https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md) — README oficial do Kata Containers (Apache-2.0) detalhando suporte a arquiteturas de 64 bits (x86_64, aarch64, ppc64le, s390x), kata-runtime check e componentes runtime, runtime-rs, agent, dragonball, osbuilder, kata-ctl e kata-deploy; consultado em 2026-10-03.
- [Kata Containers Design Documentation — Architecture & Configuration](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md) — Documentação oficial de arquitetura do Kata Containers (incluindo evolução 4.0 em Rust, containerd shimv2 e configuração de hipervisores); consultado em 2026-10-03.
- [Kata Containers — Official GitHub Repository](https://github.com/kata-containers/kata-containers) — Repositório oficial Apache-2.0 do Kata Containers; consultado em 2026-10-03.
