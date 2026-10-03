---
id: software.devops.tranche20.001956
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/Infisical/infisical/main/README.md", "https://infisical.com/docs/integrations/platforms/kubernetes/overview", "https://github.com/Infisical/infisical"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Infisical Secret Scanning e Leak Prevention (`infisical scan`): detecção preventiva de vazamentos em commits Git e pipelines CI

## Em uma frase
A CLI do Infisical inclui um motor rápido de **Secret Scanning (`infisical scan`)** projetado para varrer repositórios Git completos, intervalos de commits, arquivos staged (`git-changes`) ou diretórios em busca de chaves de API, tokens e chaves privadas expostas antes que cheguem ao repositório remoto.

## Por que importa
Uma vez que uma chave privada ou credencial de nuvem é enviada por `git push` para um repositório remoto, mesmo que seja removida no commit seguinte ela permanece no histórico Git e em caches de clones.

## Como funciona
O comando `infisical scan git-changes --staged` pode ser instalado diretamente como um hook `pre-commit` nas máquinas dos desenvolvedores para bloquear o commit localmente na origem, enquanto `infisical scan` roda no GitHub Actions/GitLab CI em todo Pull Request gerando relatórios SARIF/JSON.

## Exemplo
```bash
# Varrendo alterações staged antes do commit e instalando o hook pre-commit:
infisical scan git-changes --staged -v

# Varrendo todo o histórico de um repositório e gerando saída em JSON:
infisical scan --report-path=scan-findings.json
```

## Limites e trade-offs
Se um segredo de teste falso (mock) for sinalizado, utilize um arquivo `.infisicalignore` (ou comentários inline de ignore) versionado na raiz do repositório em vez de desabilitar o scanner na pipeline.

## Como verificar
Execute `infisical scan --no-git` em uma pasta local de configuração para validar que nenhuma credencial hardcoded está presente.

## Conexões
- [[infisical-auto-reload-deployments-annotations-rollout-zero-downtime]] — Veja também: Infisical Auto-Reload no Kubernetes: reinicialização rolling automática de `Deployments` quando segredos mudam.
- [[infisical-secret-rotation-point-in-time-recovery-honey-tokens]] — Veja também: Infisical Governança de Segredos: `Secret Rotation` automática, `Point-in-Time Recovery` e detecção de intrusão com `Honey Tokens`.

## Fontes
- [Infisical GitHub — README.md (Open-Source Secret Management, PKI, KMS & PAM Platform, CLI, Leak Prevention, Honey Tokens & Agent Vault)](https://raw.githubusercontent.com/Infisical/infisical/main/README.md) — README oficial do Infisical/infisical detalhando gerenciamento de segredos, Point-in-Time Recovery, Honey Tokens, Agent Vault, PKI, KMS e PAM; consultado em 2026-10-03.
- [Infisical Official Documentation — Kubernetes Operator Overview (v1beta1 InfisicalConnection/InfisicalAuth/InfisicalStaticSecret, Push/Dynamic Secrets & Auto-Reload)](https://infisical.com/docs/integrations/platforms/kubernetes/overview) — Documentação oficial do Infisical Kubernetes Operator cobrindo instalação Cluster-wide vs Namespace-scoped, CRDs v1beta1, auto-reload e métricas Prometheus; consultado em 2026-10-03.
- [Infisical — Official GitHub Repository](https://github.com/Infisical/infisical) — Repositório oficial MIT do Infisical; consultado em 2026-10-03.
