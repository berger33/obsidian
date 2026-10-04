---
id: software.devops.tranche10.000949
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md", "https://www.runatlantis.io/docs/locking.html", "https://www.runatlantis.io/docs/how-atlantis-works.html"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Atlantis: modelo de segurança do servidor, proteção contra PRs maliciosos, Drift Detection API e implantação em Kubernetes

## Em uma frase
A operação segura do Atlantis exige validar assinaturas de webhooks (`--gh-webhook-secret` / `--gitlab-webhook-secret`), proteger a interface web/API, persistir o diretório de dados (`--data-dir`) em um volume durável (`StatefulSet`) e compreender o lock de diretório em chamadas de API de Drift Detection (`PR: 0`).

## Por que importa
Como o servidor Atlantis detém credenciais privilegiadas para criar e destruir recursos na nuvem via Terraform e armazena em disco (`--data-dir`) os arquivos `$PLANFILE` e os metadados de locks dos PRs abertos, expor o endpoint do Atlantis na internet sem validação criptográfica de webhook ou rodar em um pod sem volume persistente causaria riscos graves de segurança ou perda de locks em restarts.

## Como funciona
(1) **Persistência (`StatefulSet`)**: em Kubernetes, o Atlantis é implantado via Helm chart oficial como um `StatefulSet` com `PersistentVolumeClaim` montado em `/atlantis-data` para preservar os locks e os planos pendentes mesmo se o pod reiniciar; (2) **Segurança de Webhooks e UI**: o servidor valida o HMAC de cada requisição de webhook do provedor Git e suporta autenticação básica/OIDC na interface web de locks; e (3) **Locking e Drift Detection (`PR: 0`)**: conforme documenta a seção `Locking and Drift Detection` em `runatlantis.io/docs/locking.html`, quando detecção ou remediação de drift roda via API com `PR: 0` (fluxo fora de PR), o Atlantis ainda adquire e libera **working directory locks** para impedir operações concorrentes no mesmo projeto, liberando-os automaticamente ao concluir sem criar locks permanentes de PR na UI.

## Exemplo
```bash
# Verificar a saúde do servidor Atlantis via endpoint /healthz e listar locks ativos
curl -sSf https://atlantis.interno.empresa.com/healthz
```

## Limites e trade-offs
Nunca exponha o servidor Atlantis a repositórios públicos abertos a Pull Requests de forks externos sem restrição, pois o Terraform executa código de inicialização de providers, módulos e blocos `local-exec` / `external` durante o `terraform init` e `terraform plan`; utilize o Atlantis apenas em repositórios privados internos com proteção de branch e revisão obrigatória.

## Como verificar
Inspecione o `StatefulSet` do Atlantis no Kubernetes (`kubectl get sts,pvc -n atlantis`) confirmando que o diretório de dados está montado em um volume persistente e que o secret de webhook está configurado.

## Conexões
- [[atlantis-verificacao-politicas-policy-checking-conftest-opa]] — Veja também: Atlantis: avaliação automatizada de políticas sobre planos Terraform (Policy Checking com Conftest / OPA Rego).
- [[atlantis-execucao-paralela-parallel-plan-apply-customizacao-bot]] — Veja também: Atlantis: execução paralela de planos (parallel_plan), customização do executável (--executable-name) e modo --verbose.
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Referência cruzada direta com atlantis-automacao-terraform-pull-requests-webhooks.
- [[atlantis-bloqueio-diretorio-workspace-locking-unlock]] — Referência cruzada direta com atlantis-bloqueio-diretorio-workspace-locking-unlock.
- [[atlantis-workflows-customizados-repos-yaml-server-side]] — Referência cruzada direta com atlantis-workflows-customizados-repos-yaml-server-side.

## Fontes
- [Atlantis Official Documentation — Using Atlantis (PR Commands plan/apply, -d/-p/-w Flags, env/{workspace}.tfvars & Automerge Flags)](https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md) — Guia oficial de uso do Atlantis detalhando comandos via comentários de PR, inclusão automática de env/{workspace}.tfvars, passagem de flags após -- e opções de automerge; consultado em 2026-10-03.
- [Atlantis Official Documentation — Locking & How Atlantis Works (Directory/Workspace Locks, Global Apply Lock, atlantis unlock & Drift Detection)](https://www.runatlantis.io/docs/locking.html) — Documentação oficial de bloqueio (Locking) do Atlantis explicando o lock por diretório e workspace até o merge do PR, Global Apply Lock fail-closed, atlantis unlock, relação com Terraform State Locking e Drift Detection; consultado em 2026-10-03.
- [RunAtlantis — Official GitHub README.md](https://www.runatlantis.io/docs/how-atlantis-works.html) — README oficial do repositório runatlantis/atlantis; consultado em 2026-10-03.
