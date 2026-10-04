---
id: software.devops.tranche11.001059
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
fontes: ["https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md", "https://polaris.docs.fairwinds.com/infrastructure-as-code/", "https://polaris.docs.fairwinds.com/admission-controller/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Migração de registro e imagens imutáveis assinadas no Fairwinds Polaris (v10.2.0+)

## Em uma frase
A partir da versão **`v10.2.0`** (`v10.1.8 → v10.2.0`), as imagens de container do Polaris migraram do registro depreciado `quay.io/fairwinds/polaris` para **`us-docker.pkg.dev/fairwinds-ops/oss/polaris`**, adotando imagens assinadas, tags imutáveis e a remoção de tags flutuantes (`v10`, `v10.1`, `latest`).

## Por que importa
Como o Polaris pode atuar como Validating e Mutating Admission Webhook dentro do cluster Kubernetes — uma posição altamente privilegiada que intercepta a criação de workloads — garantir a integridade da imagem do webhook por meio de tags imutáveis, digests SHA256 e assinatura criptográfica previne ataques à cadeia de suprimentos.

## Como funciona
Conforme o comunicado oficial em destaque no README e na documentação (`polaris.docs.fairwinds.com`), desde a release `v10.2.0`: (1) o repositório `quay.io/fairwinds/polaris` está depreciado e substituído por `us-docker.pkg.dev/fairwinds-ops/oss/polaris`; (2) não existem mais tags flutuantes como `v10`, `v10.1` ou `latest`; e (3) os usuários devem referenciar a tag de versão completa (`us-docker.pkg.dev/fairwinds-ops/oss/polaris:v<major>.<minor>.<patch>`) ou fixar pelo digest imutável (`us-docker.pkg.dev/fairwinds-ops/oss/polaris@sha256:<digest>`).

## Exemplo
```yaml
# Configuração do repositório e tag imutável do Polaris (v10.2.0+) para o Dashboard e Webhook no Kubernetes
image:
  repository: us-docker.pkg.dev/fairwinds-ops/oss/polaris
  tag: v10.2.0
  pullPolicy: IfNotPresent
```

## Limites e trade-offs
Em clusters privados sem acesso irrestrito à internet, lembre-se de liberar ou espelhar o domínio `us-docker.pkg.dev` no seu registro interno (como Harbor) antes de atualizar o chart Helm do Polaris para versões `>= v10.2.0`.

## Como verificar
Verifique a imagem em execução nos pods do namespace `polaris` com `kubectl -n polaris get pods -o jsonpath='{.items[*].spec.containers[*].image}'`.

## Conexões
- [[polaris-github-action-setup-polaris-automacao-pr]] — Veja também: Automação do Polaris no GitHub Actions com setup-polaris e verificação de Pull Requests.
- [[polaris-dashboard-auditoria-continua-cluster-scorecard]] — Veja também: Polaris Dashboard: visibilidade contínua de conformidade no cluster e combinação dos três modos de execução.
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Referência cruzada direta com polaris-motor-politicas-validacao-remediacao-kubernetes.
- [[goldilocks-migracao-registro-imagens-imutaveis-assinadas-v4-15]] — Referência cruzada direta com goldilocks-migracao-registro-imagens-imutaveis-assinadas-v4-15.
- [[pluto-migracao-registro-verificacao-cosign-checksums-v5-24]] — Referência cruzada direta com pluto-migracao-registro-verificacao-cosign-checksums-v5-24.

## Fontes
- [Fairwinds Polaris Official Documentation — Infrastructure as Code (polaris audit, polaris fix, Exit Code Flags, Helm & GitHub Action)](https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md) — Guia oficial de Infrastructure as Code do Polaris cobrindo polaris audit, polaris fix, --set-exit-code-on-danger, --set-exit-code-below-score, auditoria de Helm charts e setup-polaris GitHub Action; consultado em 2026-10-03.
- [Fairwinds Polaris Official Documentation — Admission Controller & README (Validating/Mutating Webhook, 19 Default Mutations & v10.2.0+ Images)](https://polaris.docs.fairwinds.com/infrastructure-as-code/) — Documentação oficial do Admission Controller e README do Polaris detalhando Validating Webhook (danger vs warning), Mutating Webhook (--set webhook.mutate=true com 19 mutações padrão), políticas JSON Schema e imagens imutáveis v10.2.0+; consultado em 2026-10-03.
- [Fairwinds Polaris — Official Documentation & Repository](https://polaris.docs.fairwinds.com/admission-controller/) — Documentação e repositório oficial do Fairwinds Polaris; consultado em 2026-10-03.
