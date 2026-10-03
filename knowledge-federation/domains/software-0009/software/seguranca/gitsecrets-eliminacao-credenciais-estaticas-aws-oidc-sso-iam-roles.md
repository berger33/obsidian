---
id: software.seguranca.tranche10.000980
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst", "https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Além do `git-secrets`: Como Eliminar 100% as Chaves Estáticas `AKIA...` nas Estações e no CI/CD com **AWS IAM Identity Center (SSO)** e **OIDC Federation**

## Em uma frase
Embora o `git-secrets`, o Talisman, o Gitleaks e o TruffleHog sejam indispensáveis para detectar chaves vazadas, a pergunta arquitetural mais importante de **Engenharia de Segurança Cloud** é: **por que um desenvolvedor ou um pipeline de CI/CD ainda teria uma chave de acesso estática de longa duração (`AKIA...`) salva em `~/.aws/credentials` em 2026?**

## Por que importa
Chaves IAM de longa duração (`AKIA...`) não expiram sozinhas e são a causa raiz da maioria dos comprometimentos de nuvem. A arquitetura moderna recomendada pela própria AWS substitui 100% das chaves `AKIA...` por **Credenciais Temporárias STS (`ASIA...`, com TTL curto de 15 a 60 minutos)**: **(1) Nas estações dos desenvolvedores**: autenticação via **`aws sso login` (AWS IAM Identity Center)** com MFA FIDO2/WebAuthn; **(2) Nos pipelines de CI/CD (GitHub Actions / GitLab CI)**: federação **OpenID Connect (OIDC, `AssumeRoleWithWebIdentity`)** sem nenhuma secret estática cadastrada no repositório; e **(3) Nas cargas de trabalho em produção**: **IAM Roles for Service Accounts (IRSA / EKS Pod Identity)**!

## Como funciona
Mesmo assim, observe que o `--register-aws` do `git-secrets` inclui os prefixos **`ASIA`** (chaves temporárias STS) e **`ABSK`** (Bedrock), protegendo inclusive contra o commit acidental de um token de sessão temporário ativo!

## Exemplo
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyCreateLongLivedIAMUserKeys",
      "Effect": "Deny",
      "Action": [
        "iam:CreateAccessKey",
        "iam:CreateUser"
      ],
      "Resource": "*"
    }
  ]
}
```

## Limites e trade-offs
Aplique a **Service Control Policy (SCP)** acima na sua **AWS Organizations** para proibir a criação de novos `iam:CreateAccessKey` de longa duração nas contas-membro, e audite chaves antigas remanescentes usando o **Steampipe (`aws_iam_access_key`)** ou o **Prowler**!

## Como verificar
Com `SCP (bloqueando criação de AKIA) + OIDC/SSO (emitindo apenas tokens curtos) + git-secrets/Talisman (bloqueando commits locais)`, você fecha o ciclo completo de prevenção.

## Conexões
- [[gitsecrets-integracao-pipelines-cicd-github-actions-gitlab-pre-receive]] — Veja também: Implantação de `git-secrets` em **Pipelines CI/CD** e **Hooks Server-Side (`pre-receive`)** para Impedir Bypass com `git commit --no-verify`.
- [[gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider]] — Referência cruzada direta com gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider.
- [[steampipe-joins-multi-cloud-aws-gcp-kubernetes-github-iam]] — Referência cruzada direta com steampipe-joins-multi-cloud-aws-gcp-kubernetes-github-iam.

## Fontes
- [AWS Labs git-secrets Official Documentation (`README.rst`) — CLI Reference, `--register-aws`, Bedrock Keys & `.gitallowed`](https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst) — documentação oficial do `git-secrets` cobrindo instalação dos 3 hooks (`pre-commit`, `commit-msg`, `prepare-commit-msg`), `--register-aws`, `--aws-provider`, `--scan-history` e `.gitallowed`; consultado em 2026-10-03.
- [AWS Labs git-secrets Official Implementation (`git-secrets`) — Hook Internals & Git-Grep Engine](https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets) — código-fonte oficial do `git-secrets` mostrando o funcionamento interno de `pre_commit_hook`, `commit_msg_hook`, `prepare_commit_msg_hook` e `scan_history`; consultado em 2026-10-03.
