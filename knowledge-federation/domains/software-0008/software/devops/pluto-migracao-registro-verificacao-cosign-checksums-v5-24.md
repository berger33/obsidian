---
id: software.devops.tranche11.001068
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://pluto.docs.fairwinds.com/installation/", "https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md", "https://pluto.docs.fairwinds.com/quickstart/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cadeia de suprimentos do Pluto (v5.24.0+): migração para Artifact Registry, tags imutáveis e verificação com Cosign

## Em uma frase
A partir da versão **`v5.24.0`** (`v5.23.6 → v5.24.0`), as imagens de container do Pluto migraram de `quay.io/fairwinds/pluto` para **`us-docker.pkg.dev/fairwinds-ops/oss/pluto`** com tags imutáveis (`v<major>.<minor>.<patch>`), e tanto a imagem quanto o arquivo `checksums.txt` de releases podem ser verificados criptograficamente com **Cosign** usando a chave pública oficial `https://artifacts.fairwinds.com/cosign.pub`.

## Por que importa
Em pipelines de CI/CD corporativos ou CronJobs de auditoria que executam o Pluto com acesso de leitura a todos os Secrets de releases Helm do cluster, verificar a assinatura criptográfica do binário (`cosign verify-blob`) ou da imagem de container (`cosign verify`) garante que o artefato baixado é autêntico e não foi adulterado.

## Como funciona
Conforme documentam o README oficial (`FairwindsOps/pluto`) e a página *Installation — Verify Artifacts* (`pluto.docs.fairwinds.com/installation/`): (1) a Fairwinds assina a imagem Docker do Pluto e o arquivo `checksums.txt` com o **Sigstore Cosign**, disponibilizando a chave pública em `https://artifacts.fairwinds.com/cosign.pub`; (2) para validar os binários de release, usa-se `cosign verify-blob checksums.txt --signature=checksums.txt.sig --key https://artifacts.fairwinds.com/cosign.pub`; (3) para validar a imagem de container, usa-se `cosign verify`; e (4) desde a `v5.24.0`, tags flutuantes (`v5`, `v5.23`, `latest`) não são mais publicadas, exigindo tags semânticas completas ou digest `@sha256:<digest>`.

## Exemplo
```bash
# Verificar a assinatura criptográfica do arquivo checksums.txt e da imagem OCI do Pluto usando Cosign
cosign verify-blob checksums.txt \
  --signature=checksums.txt.sig \
  --key https://artifacts.fairwinds.com/cosign.pub

cosign verify us-docker.pkg.dev/fairwinds-ops/oss/pluto:v5.24.0 \
  --key https://artifacts.fairwinds.com/cosign.pub
```

## Limites e trade-offs
Pipelines de CI ou manifestos de CronJob que ainda utilizavam `quay.io/fairwinds/pluto:latest` ou `:v5` precisam ser atualizados para `us-docker.pkg.dev/fairwinds-ops/oss/pluto:v<major>.<minor>.<patch>` para continuar recebendo o catálogo atualizado de depreciações do Kubernetes.

## Como verificar
Execute o comando `cosign verify` acima em uma estação com `cosign` instalado e confirme o retorno do payload JSON de assinatura válida da Fairwinds.

## Conexões
- [[pluto-instalacao-asdf-homebrew-scoop-binarios]] — Veja também: Métodos de instalação do Pluto: plugin asdf, Homebrew Tap, binários de release e Scoop.
- [[pluto-exemplos-classicos-ingress-webhook-psp-migracao]] — Veja também: Casos reais de detecção do Pluto: MutatingWebhookConfiguration, Ingress (v1beta1 -> v1) e PodSecurityPolicy.
- [[goldilocks-migracao-registro-imagens-imutaveis-assinadas-v4-15]] — Referência cruzada direta com goldilocks-migracao-registro-imagens-imutaveis-assinadas-v4-15.

## Fontes
- [Fairwinds Pluto GitHub — README.md & QuickStart (API Server Conversion Pitfall, Deprecation Policy, detect-files, detect-helm & detect-all-in-cluster)](https://pluto.docs.fairwinds.com/installation/) — README e QuickStart oficiais do Fairwinds Pluto explicando a armadilha de conversão de versão do kube-apiserver, diferença entre DEPRECATED e REMOVED e uso de detect-files, detect-helm, detect-api-resources e detect-all-in-cluster; consultado em 2026-10-03.
- [Fairwinds Pluto Official Documentation — Installation & Artifact Verification (asdf, Homebrew, Cosign Verification & v5.24.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md) — Guia oficial de instalação do Pluto documentando plugin asdf, Homebrew Tap, verificação de assinatura criptográfica com Cosign (verify-blob e verify) e migração para imagens imutáveis na v5.24.0+; consultado em 2026-10-03.
- [Fairwinds Pluto — Official Documentation & Repository](https://pluto.docs.fairwinds.com/quickstart/) — Documentação e repositório oficial do Fairwinds Pluto; consultado em 2026-10-03.
