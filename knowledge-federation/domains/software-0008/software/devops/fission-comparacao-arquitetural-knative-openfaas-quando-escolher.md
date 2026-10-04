---
id: software.devops.tranche19.001820
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
fontes: ["https://fission.io/docs/concepts/", "https://raw.githubusercontent.com/fission/fission/main/README.md", "https://github.com/fission/fission"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fission vs Knative e OpenFaaS: critérios arquiteturais de *cold start*, peso operacional e experiência de código

## Em uma frase
A documentação oficial de conceitos do Fission compara diretamente a arquitetura do Fission com **Knative**, **OpenFaaS** e FaaS gerenciado sob três eixos: latência de *cold start*, peso operacional no cluster e abstração de containers ("*just the code*" vs construir imagens por função).

## Por que importa
Escolher uma plataforma serverless que exige instalar um service mesh completo e construir uma imagem OCI a cada linha alterada pode ser excessivo para equipes que querem apenas implantar funções rápidas de integração ou automação em Kubernetes.

## Como funciona
O Fission destaca-se quando você quer: 1) operar diretamente sobre o código-fonte (`--code` / `specs/`) com Docker e Kubernetes abstraídos na operação normal; 2) *cold starts* de ~100 ms via pools aquecidos (`poolmgr`); e 3) coexistência no mesmo cluster entre funções rápidas (`poolmgr`), APIs escaladas por HPA (`newdeploy`) e containers customizados (`container`).

## Exemplo
```bash
# Verificando a saúde e versão de todos os serviços da instalação Fission:
fission version
fission check
```

## Limites e trade-offs
O comando `fission check` executa diagnósticos pré-voo e pós-instalação verificando a versão do Kubernetes, permissões RBAC e prontidão de todos os Pods de controle do Fission.

## Como verificar
Execute `fission check` no cluster para confirmar que todos os componentes do Fission passam nas verificações operacionais.

## Conexões
- [[fission-container-executor-execucao-imagens-oci-customizadas-scale-zero]] — Veja também: Fission `container` Executor: execução de imagens OCI arbitrárias com scale-to-zero no Fission.

## Fontes
- [Fission GitHub — README.md (Serverless Functions for Kubernetes, 100msec Warm Pool Cold Start & CLI Quickstart)](https://fission.io/docs/concepts/) — README oficial do fission/fission detalhando o modelo de pools de containers aquecidos (~100 ms cold start) e comandos fission env/function; consultado em 2026-10-03.
- [Fission Official Documentation — Concepts (Functions, Environments, Executors, Triggers, Packages & Declarative Specs)](https://raw.githubusercontent.com/fission/fission/main/README.md) — Documentação oficial de conceitos do Fission explicando a relação entre Trigger, Function, Environment e Package e os executores poolmgr/newdeploy/container; consultado em 2026-10-03.
- [Fission — Official GitHub Repository](https://github.com/fission/fission) — Repositório oficial Apache-2.0 do Fission para Kubernetes; consultado em 2026-10-03.
