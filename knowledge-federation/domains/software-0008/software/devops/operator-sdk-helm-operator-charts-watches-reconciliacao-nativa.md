---
id: software.devops.tranche18.001754
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

# Operator SDK `helm-operator`: conversão de Helm Charts existentes em Operators Kubernetes declarativos

## Em uma frase
No fluxo de **Helm Operator** do Operator SDK (`--plugins=helm`), o binário `helm-operator` embute um Helm Chart dentro da imagem do operador (em `helm-charts/<kind>/`) e reconcilia automaticamente cada instância de Custom Resource aplicando seu `spec` como overrides sobre o `values.yaml` do chart.

## Por que importa
Distribuir um Helm Chart complexo diretamente aos usuários finais exige que cada desenvolvedor gerencie versões do CLI `helm` e valores de release; encapsular o chart em um Helm Operator expõe uma API CRD limpa controlada por RBAC e reconciliada continuamente contra desvios (*drift*).

## Como funciona
O comando `operator-sdk create api --group app --version v1alpha1 --kind Nginx --helm-chart=...` importa o chart (novo, de diretório local ou de repositório Helm), gera o CRD para o GVK e registra o mapeamento em `watches.yaml`. Sempre que o CR ou qualquer recurso filho do release Helm sofre alteração, o `helm-operator` reexecuta a reconciliação.

## Exemplo
```bash
operator-sdk init --plugins=helm --domain=example.com
operator-sdk create api --group web --version v1alpha1 --kind Frontend
ls -la helm-charts/frontend/ watches.yaml
```

## Limites e trade-offs
Para inspecionar a versão exata do Kubernetes e do `client-go` suportada pela imagem base de um Helm Operator, execute `docker run --entrypoint helm-operator quay.io/operator-framework/helm-operator:<tag> version`.

## Como verificar
Construa o projeto Helm Operator de teste e verifique em `watches.yaml` o vínculo entre o GVK criado e o diretório `helm-charts/`.

## Conexões
- [[operator-sdk-ansible-operator-watches-yaml-roles-playbooks]] — Veja também: Operator SDK `ansible-operator`: reconciliação de Custom Resources via `watches.yaml`, Roles e Playbooks Ansible.
- [[operator-sdk-olm-integration-operator-sdk-olm-install-status]] — Veja também: Operator SDK e OLM (*Operator Lifecycle Manager*): instalação, verificação de status e matriz de compatibilidade.

## Fontes
- [Operator SDK GitHub — README.md (Operator Framework Toolkit, Controller-Runtime Integration & Metrics Authn/Authz Notice)](https://sdk.operatorframework.io/docs/overview/) — README oficial do operator-framework/operator-sdk detalhando a arquitetura do SDK e a substituição do kube-rbac-proxy por WithAuthenticationAndAuthorization; consultado em 2026-10-03.
- [Operator SDK Official Documentation — Overview (Go/Ansible/Helm Workflows, 5 Capability Levels, Kubernetes/client-go & OLM Compatibility)](https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md) — Documentação oficial Overview do Operator SDK cobrindo fluxos Go/Ansible/Helm, 5 níveis de maturidade, versões embutidas do OLM e suporte multi-arquitetura; consultado em 2026-10-03.
- [Operator SDK — Official GitHub Repository](https://github.com/operator-framework/operator-sdk) — Repositório oficial Apache-2.0 do Operator SDK na CNCF; consultado em 2026-10-03.
