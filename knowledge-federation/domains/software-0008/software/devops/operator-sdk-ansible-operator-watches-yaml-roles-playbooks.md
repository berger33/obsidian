---
id: software.devops.tranche18.001753
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://sdk.operatorframework.io/docs/overview/", "https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md", "https://github.com/operator-framework/operator-sdk"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Operator SDK `ansible-operator`: reconciliação de Custom Resources via `watches.yaml`, Roles e Playbooks Ansible

## Em uma frase
No fluxo de **Ansible Operator** do Operator SDK (`--plugins=ansible`), o motor binário `ansible-operator` (escrito em Go sobre `controller-runtime`) observa eventos de Custom Resources no Kubernetes e executa **Ansible Roles** ou **Playbooks** mapeados no arquivo `watches.yaml`, injetando todos os campos de `spec` do CR como variáveis Ansible.

## Por que importa
Equipes de SRE e banco de dados que já automatizam rotinas de backup, tuning e configuração com módulos Ansible (`kubernetes.core.k8s`) podem empacotar essa inteligência diretamente dentro de um Operator Kubernetes.

## Como funciona
Ao executar `operator-sdk init --plugins=ansible --domain=example.com` e `operator-sdk create api --group cache --version v1alpha1 --kind Memcached --generate-role`, o SDK gera a estrutura `roles/memcached/` e adiciona uma entrada em `watches.yaml` ligando o GVK `cache.example.com/v1alpha1, Kind=Memcached` à role correspondente.

## Exemplo
```yaml
# watches.yaml em um Ansible Operator:
---
- version: v1alpha1
  group: cache.example.com
  kind: Memcached
  role: memcached
  reconcilePeriod: 0s
  manageStatus: true
```

## Limites e trade-offs
Nomes de campos em `camelCase` dentro do `spec` do Custom Resource YAML (ex.: `replicaCount: 3`) são convertidos automaticamente pelo `ansible-operator` para `snake_case` (`replica_count`) ao serem passados como variáveis para a role Ansible.

## Como verificar
Verifique a versão do runtime com `docker run --entrypoint ansible-operator quay.io/operator-framework/ansible-operator:latest version` e valide o arquivo `watches.yaml`.

## Conexões
- [[operator-sdk-modelo-maturidade-5-capability-levels-go-ansible-helm]] — Veja também: Operator SDK: modelo de maturidade de 5 níveis (*Operator Capability Levels*) e comparação entre Go, Ansible e Helm.
- [[operator-sdk-helm-operator-charts-watches-reconciliacao-nativa]] — Veja também: Operator SDK `helm-operator`: conversão de Helm Charts existentes em Operators Kubernetes declarativos.

## Fontes
- [Operator SDK GitHub — README.md (Operator Framework Toolkit, Controller-Runtime Integration & Metrics Authn/Authz Notice)](https://sdk.operatorframework.io/docs/overview/) — README oficial do operator-framework/operator-sdk detalhando a arquitetura do SDK e a substituição do kube-rbac-proxy por WithAuthenticationAndAuthorization; consultado em 2026-10-03.
- [Operator SDK Official Documentation — Overview (Go/Ansible/Helm Workflows, 5 Capability Levels, Kubernetes/client-go & OLM Compatibility)](https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md) — Documentação oficial Overview do Operator SDK cobrindo fluxos Go/Ansible/Helm, 5 níveis de maturidade, versões embutidas do OLM e suporte multi-arquitetura; consultado em 2026-10-03.
- [Operator SDK — Official GitHub Repository](https://github.com/operator-framework/operator-sdk) — Repositório oficial Apache-2.0 do Operator SDK na CNCF; consultado em 2026-10-03.
