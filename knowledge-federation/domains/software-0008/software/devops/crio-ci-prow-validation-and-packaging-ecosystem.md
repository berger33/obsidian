---
id: software.devops.tranche04.000380
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/cri-o/cri-o/main/README.md", "https://cri-o.github.io/cri-o", "https://github.com/cri-o/cri-o"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Validação contínua em GitHub Actions e OpenShift Prow e pacotes DEB/RPM do CRI-O

## Em uma frase
O repositório oficial do CRI-O detalha que sua integração contínua é dividida entre **GitHub Actions** e **OpenShift CI (Prow)** (`prow.ci.openshift.org`), mantendo jobs periódicos automatizados (`periodic-ci-cri-o-cri-o-main-periodics-setup-periodic`, `setup-fedora-periodic`, `evented-pleg-periodic`) definidos no repositório `openshift/release`. Para instalação em produção, o projeto mantém o repositório oficial de empacotamento **`cri-o/packaging`** (`github.com/cri-o/packaging`) com pacotes **DEB e RPM** oficiais, além de publicar relatórios contínuos de dependências (`cri-o.github.io/cri-o/dependencies`).

## Por que importa
Como o runtime de contêiner é o componente mais crítico de cada nó trabalhador Kubernetes, contar com pacotes DEB/RPM oficiais assinados e validados continuamente contra a suíte de conformidade do Kubernetes e OpenShift Prow reduz o risco de regressões em nível de sistema operacional.

## Como funciona
Instale o CRI-O nos nós Linux a partir dos repositórios de pacotes DEB/RPM oficiais mantidos em `github.com/cri-o/packaging` alinhados à versão minor do Kubernetes do cluster, em vez de compilar binários manualmente em servidores de produção.

## Exemplo
Durante a construção automatizada das imagens de máquina (AMIs/golden images) dos nós Kubernetes com Packer, o script adiciona o repositório oficial `cri-o/packaging` da série minor alvo e instala o pacote `cri-o` homologado.

## Limites e trade-offs
Evite misturar pacotes do CRI-O de repositórios não oficiais de terceiros com versões dispares de `conmon`, `runc`/`crun` e plugins CNI; utilize os pacotes integrados da distribuição ou de `cri-o/packaging`.

## Como verificar
Verifique a origem e a versão do pacote instalado (`rpm -qi cri-o` ou `apt-cache policy cri-o`) confirmando sua correspondência com a release oficial publicada pelo projeto.

## Conexões
- [[crio-metrics-tracing-and-evented-pleg-observability]] — Veja também: Observabilidade do CRI-O com métricas Prometheus, tracing distribuído e Evented PLEG.

## Fontes
- [CRI-O GitHub — README.md (Kubernetes Compatibility Matrix, Scope, Config & HTTP Status API)](https://raw.githubusercontent.com/cri-o/cri-o/main/README.md) — README oficial do CRI-O detalhando alinhamento de versões 1.x.y e política de version skew n-2 com o Kubernetes, escopo estrito de implementação da CRI para o Kubelet, bibliotecas OCI (runc, container-libs/image, container-libs/storage, CNI), arquivos crio.conf, policy.json, registries.conf, storage.conf e API de status via crio status e socket /var/run/crio/crio.sock.; consultado em 2026-10-03.
- [CRI-O — Official Release Notes & Documentation Portal](https://cri-o.github.io/cri-o) — Portal oficial de notas de versão e relatórios de dependências do CRI-O mantido pelos desenvolvedores do projeto.; consultado em 2026-10-03.
- [CRI-O — Official GitHub Repository](https://github.com/cri-o/cri-o) — Repositório oficial Apache-2.0 do CRI-O na CNCF.; consultado em 2026-10-03.
