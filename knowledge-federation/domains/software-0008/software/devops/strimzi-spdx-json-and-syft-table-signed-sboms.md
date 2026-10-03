---
id: software.devops.tranche05.000456
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

# Publicação e verificação de SBOMs assinados do Strimzi nos formatos SPDX-JSON e Syft-Table

## Em uma frase
A seção *Software Bill of Materials (SBOM)* do README oficial informa que, desde a release **0.38.0**, o Strimzi publica o SBOM de todos os seus contêineres como um arquivo pacote contendo os formatos **`SPDX-JSON` e `Syft-Table`** assinados com Cosign (e também enviados ao registro de contêineres nas releases oficiais). Assim como nas imagens, desde a release **0.49.0** a assinatura dos SBOMs utiliza o modo **keyless** do Cosign, sendo verificada com: `cosign verify-blob --bundle <SBOM-file>.bundle --certificate-identity-regexp='https://github.com/strimzi/.*' --certificate-oidc-issuer='https://token.actions.githubusercontent.com' <SBOM-file>`.

## Por que importa
Quando uma nova vulnerabilidade crítica é divulgada no ecossistema Java, OpenSSL ou Linux, os administradores do Strimzi podem inspecionar imediatamente os arquivos SBOM `SPDX-JSON` e `Syft-Table` oficiais (por exemplo usando `grype` ou `jq`) após validar sua autenticidade com `cosign verify-blob`, sem precisar escanear todas as imagens pesadas manualmente.

## Como funciona
Baixe o arquivo de SBOM e seu respectivo `.bundle` da release do Strimzi instalada em produção, valide a assinatura com `cosign verify-blob` e arquive o `SPDX-JSON` no inventário de conformidade e monitoramento contínuo de CVEs da empresa.

## Exemplo
Durante um alerta de segurança sobre uma biblioteca Java, a equipe de segurança valida o pacote SBOM da release do Strimzi com `cosign verify-blob` e consulta o arquivo `SPDX-JSON` para comprovar em segundos a versão exata da biblioteca presente na imagem do broker.

## Limites e trade-offs
Para SBOMs de releases anteriores à `0.49.0`, utilize o comando com chave pública documentado no README: `cosign verify-blob --key cosign.pub --bundle <SBOM-file>.bundle --insecure-ignore-tlog=true <SBOM-file>`.

## Como verificar
Baixe o SBOM e o bundle de uma release oficial do Strimzi e execute `cosign verify-blob` confirmando a mensagem `Verified OK`.

## Conexões
- [[strimzi-cosign-keyless-container-signature-verification]] — Veja também: Verificação de assinaturas de imagens do Strimzi com Cosign (keyless desde a versão 0.49.0).
- [[strimzi-minikube-versus-kubernetes-kind-local-tradeoffs]] — Veja também: Diferenças operacionais entre Minikube e Kubernetes Kind para clusters locais do Strimzi.

## Fontes
- [Strimzi GitHub — README.md (Apache Kafka on Kubernetes/OpenShift, Cosign Keyless Signatures, SBOM & DCO)](https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md) — README oficial do Strimzi (Apache-2.0) detalhando operação de Apache Kafka no Kubernetes e OpenShift, assinatura de contêineres com Cosign (a partir da 0.38.0 e keyless desde a 0.49.0), publicação e verificação de SBOM em SPDX-JSON e Syft-Table, guias de desenvolvimento/teste e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [Strimzi Official Documentation — Quick Starts (CRDs, Namespace Matching, Producer/Consumer & PVC Cleanup)](https://strimzi.io/quickstarts/) — Guia oficial de início rápido do Strimzi detalhando instalação do Cluster Operator com strimzi.io/install/latest?namespace=kafka, CRDs Kafka e KafkaTopic, envio e consumo de mensagens via my-cluster-kafka-bootstrap:9092 e obrigatoriedade de deletar PVCs residuais ao recriar clusters.; consultado em 2026-10-03.
- [Strimzi — Official GitHub Repository](https://github.com/strimzi/strimzi-kafka-operator) — Repositório oficial Apache-2.0 do Strimzi Kafka Operator.; consultado em 2026-10-03.
