---
id: software.devops.tranche05.000455
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

# Verificação de assinaturas de imagens do Strimzi com Cosign (keyless desde a versão 0.49.0)

## Em uma frase
A seção *Container signatures* do README oficial documenta a segurança da cadeia de suprimentos das imagens do Strimzi: desde a release **0.38.0**, todos os contêineres do Strimzi são assinados usando a ferramenta **Sigstore Cosign**, e desde a release **0.49.0** o projeto passou a adotar **assinatura keyless (sem chaves estáticas)**. Para verificar as imagens da versão 0.49.0 em diante, executa-se: `cosign verify --certificate-identity-regexp='https://github.com/strimzi/.*' --certificate-oidc-issuer='https://token.actions.githubusercontent.com' quay.io/strimzi/operator:latest` (enquanto versões anteriores à 0.49.0 são verificadas com a chave pública oficial `strimzi.pub` e `--insecure-ignore-tlog=true`).

## Por que importa
Como o operador do Strimzi e as imagens dos brokers Kafka detêm acesso privilegiado aos fluxos de eventos e segredos de autenticação do cluster, validar criptograficamente que as imagens em `quay.io/strimzi/*` foram construídas pelo workflow oficial do GitHub Actions da organização `strimzi` impede ataques de adulteração de imagem.

## Como funciona
Configure políticas de verificação de imagem (por exemplo, no Kyverno, Connaisseur ou CRI-O `policy.json`) ou etapas de gate no pipeline usando a expressão `--certificate-identity-regexp='https://github.com/strimzi/.*'` e `--certificate-oidc-issuer='https://token.actions.githubusercontent.com'` para releases `>= 0.49.0`.

## Exemplo
Antes de espelhar uma nova release do Strimzi para o registro privado corporativo, o pipeline de plataforma executa `cosign verify` com os parâmetros keyless oficiais contra as imagens do operador e do Kafka.

## Limites e trade-offs
Ao verificar imagens legadas do Strimzi de versões entre `0.38.0` e `0.48.x`, lembre-se de que elas utilizavam assinatura baseada em chave (`--key strimzi.pub --insecure-ignore-tlog=true`) e não o fluxo OIDC keyless introduzido na `0.49.0`.

## Como verificar
Execute o comando `cosign verify` documentado no README contra a imagem da release atual do Strimzi e confirme o retorno válido dos claims assinados.

## Conexões
- [[strimzi-pvc-cleanup-requirement-on-cluster-deletion]] — Veja também: Exclusão explícita de PersistentVolumeClaims (PVCs) ao remover e recriar clusters Kafka no Strimzi.
- [[strimzi-spdx-json-and-syft-table-signed-sboms]] — Veja também: Publicação e verificação de SBOMs assinados do Strimzi nos formatos SPDX-JSON e Syft-Table.

## Fontes
- [Strimzi GitHub — README.md (Apache Kafka on Kubernetes/OpenShift, Cosign Keyless Signatures, SBOM & DCO)](https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md) — README oficial do Strimzi (Apache-2.0) detalhando operação de Apache Kafka no Kubernetes e OpenShift, assinatura de contêineres com Cosign (a partir da 0.38.0 e keyless desde a 0.49.0), publicação e verificação de SBOM em SPDX-JSON e Syft-Table, guias de desenvolvimento/teste e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [Strimzi Official Documentation — Quick Starts (CRDs, Namespace Matching, Producer/Consumer & PVC Cleanup)](https://strimzi.io/quickstarts/) — Guia oficial de início rápido do Strimzi detalhando instalação do Cluster Operator com strimzi.io/install/latest?namespace=kafka, CRDs Kafka e KafkaTopic, envio e consumo de mensagens via my-cluster-kafka-bootstrap:9092 e obrigatoriedade de deletar PVCs residuais ao recriar clusters.; consultado em 2026-10-03.
- [Strimzi — Official GitHub Repository](https://github.com/strimzi/strimzi-kafka-operator) — Repositório oficial Apache-2.0 do Strimzi Kafka Operator.; consultado em 2026-10-03.
