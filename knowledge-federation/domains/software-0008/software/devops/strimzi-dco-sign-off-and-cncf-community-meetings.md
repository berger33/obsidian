---
id: software.devops.tranche05.000460
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md", "https://strimzi.io/quickstarts/", "https://github.com/strimzi/strimzi-kafka-operator"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Conformidade DCO (git commit -s / git commit --amend -s) e reuniões comunitárias do Strimzi

## Em uma frase
O README oficial do Strimzi exige que todos os commits submetidos ao projeto sejam assinados com o **Developer Certificate of Origin (DCO)** (`developercertificate.org`) adicionando a linha **`Signed-off-by: Name <email>`** à mensagem do commit por meio de **`git commit -s -m '...'`** (ou corrigindo o último commit esquecido com **`git commit --amend -s`**). O projeto também realiza reuniões comunitárias regulares abertas a cada 4 semanas às quintas-feiras em dois horários alternados (09:00 UTC e 16:00 UTC, defasados em 2 semanas para atender diferentes fusos horários) com pauta pública e gravações no YouTube.

## Por que importa
A assinatura DCO atesta formalmente que o autor tem o direito de licenciar a contribuição sob a licença Apache-2.0 do projeto, requisito obrigatório para projetos da CNCF.

## Como funciona
Use sempre a flag `-s` em `git commit -s` ao contribuir código ou documentação para o Strimzi e utilize `git commit --amend -s` imediatamente caso um commit local tenha sido criado sem a linha `Signed-off-by:`.

## Exemplo
Após abrir um PR e notar que o check do DCO falhou porque o commit não continha o rodapé exigido, o contribuidor executa `git commit --amend -s` e atualiza a branch do PR, aprovando a verificação automatizada.

## Limites e trade-offs
Certifique-se de que o nome e o e-mail na linha `Signed-off-by:` correspondem aos metadados de autor do commit Git para evitar rejeição pelo bot verificador do DCO.

## Como verificar
Inspecione o histórico da branch com `git log -n 3` antes do push para garantir que todos os commits incluem a linha `Signed-off-by:` válida.

## Conexões
- [[strimzi-development-testing-and-release-guides-workflow]] — Veja também: Fluxo de build, guia de testes (TESTING.md) e checklist de release no repositório do Strimzi.

## Fontes
- [Strimzi GitHub — README.md (Apache Kafka on Kubernetes/OpenShift, Cosign Keyless Signatures, SBOM & DCO)](https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md) — README oficial do Strimzi (Apache-2.0) detalhando operação de Apache Kafka no Kubernetes e OpenShift, assinatura de contêineres com Cosign (a partir da 0.38.0 e keyless desde a 0.49.0), publicação e verificação de SBOM em SPDX-JSON e Syft-Table, guias de desenvolvimento/teste e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [Strimzi Official Documentation — Quick Starts (CRDs, Namespace Matching, Producer/Consumer & PVC Cleanup)](https://strimzi.io/quickstarts/) — Guia oficial de início rápido do Strimzi detalhando instalação do Cluster Operator com strimzi.io/install/latest?namespace=kafka, CRDs Kafka e KafkaTopic, envio e consumo de mensagens via my-cluster-kafka-bootstrap:9092 e obrigatoriedade de deletar PVCs residuais ao recriar clusters.; consultado em 2026-10-03.
- [Strimzi — Official GitHub Repository](https://github.com/strimzi/strimzi-kafka-operator) — Repositório oficial Apache-2.0 do Strimzi Kafka Operator.; consultado em 2026-10-03.
