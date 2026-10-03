---
id: software.devops.tranche18.001758
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

# Operator SDK `scorecard`: validação automatizada de bundles com suítes básicas, OLM e testes declarativos KUTTL

## Em uma frase
A ferramenta **`operator-sdk scorecard`** executa Pods de teste dentro do cluster Kubernetes para validar se o pacote Bundle de um operador segue as melhores práticas do Operator Framework, utilizando as imagens oficiais `scorecard-test` e `scorecard-test-kuttl`.

## Por que importa
Mesmo que um bundle passe na validação estática de arquivos YAML (`bundle validate`), ele pode falhar em tempo de execução se os exemplos em `alm-examples` do CSV forem inválidos ou se o operador não preencher o bloco `status` após reconciliar um CR.

## Como funciona
Configurado em `bundle/tests/scorecard/config.yaml` (gerado automaticamente por `make bundle`), o `scorecard` roda estágios em paralelo ou sequência: a suíte **basic** (`basic-check-spec-test`), a suíte **olm** (`olm-bundle-validation-test`, `olm-crds-have-validation-test`, `olm-crds-have-resources-test`, `olm-spec-descriptors-test`, `olm-status-descriptors-test`) e testes de integração ponta a ponta com **KUTTL** (`scorecard-test-kuttl`).

## Exemplo
```bash
operator-sdk scorecard ./bundle \
  --kubeconfig ~/.kube/config \
  --namespace default \
  --wait-time 120s
```

## Limites e trade-offs
Conforme documentado na matriz oficial de plataformas do Operator SDK, a imagem `scorecard-test` é publicada para `linux/amd64`, `linux/arm64`, `linux/ppc64le` e `linux/s390x`, enquanto `scorecard-test-kuttl` é publicada para `linux/amd64`, `linux/arm64` e `linux/ppc64le`.

## Como verificar
Inspecione `bundle/tests/scorecard/config.yaml` e execute `operator-sdk scorecard ./bundle` contra um cluster de teste.

## Conexões
- [[operator-sdk-run-bundle-run-bundle-upgrade-testes-ciclo-vida-olm]] — Veja também: Operator SDK `run bundle` e `run bundle-upgrade`: validação ponta a ponta de instalação e upgrade no OLM.
- [[operator-sdk-matriz-compatibilidade-kubernetes-client-go-lookup]] — Veja também: Operator SDK: auditoria de compatibilidade de versões com Kubernetes e `client-go` por tipo de projeto.

## Fontes
- [Operator SDK GitHub — README.md (Operator Framework Toolkit, Controller-Runtime Integration & Metrics Authn/Authz Notice)](https://sdk.operatorframework.io/docs/overview/) — README oficial do operator-framework/operator-sdk detalhando a arquitetura do SDK e a substituição do kube-rbac-proxy por WithAuthenticationAndAuthorization; consultado em 2026-10-03.
- [Operator SDK Official Documentation — Overview (Go/Ansible/Helm Workflows, 5 Capability Levels, Kubernetes/client-go & OLM Compatibility)](https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md) — Documentação oficial Overview do Operator SDK cobrindo fluxos Go/Ansible/Helm, 5 níveis de maturidade, versões embutidas do OLM e suporte multi-arquitetura; consultado em 2026-10-03.
- [Operator SDK — Official GitHub Repository](https://github.com/operator-framework/operator-sdk) — Repositório oficial Apache-2.0 do Operator SDK na CNCF; consultado em 2026-10-03.
