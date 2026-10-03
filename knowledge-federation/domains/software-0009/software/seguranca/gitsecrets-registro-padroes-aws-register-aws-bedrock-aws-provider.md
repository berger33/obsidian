---
id: software.seguranca.tranche10.000972
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

# `git-secrets` **`--register-aws` & `--aws-provider`**: Detecção de Prefixos IAM (`AKIA`, `ASIA`, `AROA`), Chaves **Amazon Bedrock (`ABSK`)** e Leitura de `~/.aws/credentials`

## Em uma frase
O comando **`git secrets --register-aws`** (ou `git secrets --register-aws --global`) popula automaticamente a configuração do Git (`secrets.patterns`, `secrets.allowed` e `secrets.providers`) com o conjunto oficial de regras da AWS.

## Por que importa
Conforme documentado no `README.rst` oficial atualizado do projeto, o `--register-aws` adiciona cinco camadas de verificação: **(1) Prefixos de IDs de Chaves AWS**: `(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}` (cobrindo chaves IAM permanentes `AKIA`, credenciais temporárias STS `ASIA`, Roles `AROA`, etc.); **(2) Chaves de API do Amazon Bedrock**: tanto chaves de longa duração (`ABSK[A-Za-z0-9+/]{109,}=*`) quanto chaves de curta duração (`bedrock-api-key-YmVkcm9jay5hbWF6b25hd3MuY29t`); **(3) Atribuições de `AWS Secret Access Key` e `Account ID`**; **(4) Exceções automáticas para as chaves de exemplo da documentação da AWS** (`AKIAIOSFODNN7EXAMPLE` e `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`); e **(5) O Provedor Dinâmico `--aws-provider`**!

## Como funciona
O que o **`git secrets --aws-provider`** faz a cada commit? Ele lê em tempo real o arquivo local **`~/.aws/credentials`** da máquina do desenvolvedor, extrai os valores literais das chaves secretas configuradas lá e **bloqueia o commit imediatamente se qualquer uma das chaves reais da máquina aparecer no código**!

## Exemplo
```bash
# Registrar globalmente os padroes oficiais da AWS e testar o provedor que extrai segredos de ~/.aws/credentials
git secrets --register-aws --global
git secrets --aws-provider
```

## Limites e trade-offs
Você também pode passar o caminho de um arquivo INI customizado para o `--aws-provider`: por exemplo, `git secrets --add-provider -- git secrets --aws-provider /caminho/credenciais_extras.ini`!

## Como verificar
Verifique todas as expressões registradas no seu `~/.gitconfig` executando `git secrets --list --global`.

## Conexões
- [[gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep]] — Veja também: **awslabs `git-secrets` (`awslabs/git-secrets`)**: Arquitetura dos **3 Hooks Git (`pre-commit`, `commit-msg`, `prepare-commit-msg`)** e Subcomando Nativo `git secrets`.
- [[gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos]] — Veja também: `git-secrets`: Adição de Padrões Proibidos (`--add`), Literais (`--literal`), Exceções (`.gitallowed` / `--allowed`) e **Secret Providers (`--add-provider`)**.

## Fontes
- [AWS Labs git-secrets Official Documentation (`README.rst`) — CLI Reference, `--register-aws`, Bedrock Keys & `.gitallowed`](https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst) — documentação oficial do `git-secrets` cobrindo instalação dos 3 hooks (`pre-commit`, `commit-msg`, `prepare-commit-msg`), `--register-aws`, `--aws-provider`, `--scan-history` e `.gitallowed`; consultado em 2026-10-03.
- [AWS Labs git-secrets Official Implementation (`git-secrets`) — Hook Internals & Git-Grep Engine](https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets) — código-fonte oficial do `git-secrets` mostrando o funcionamento interno de `pre_commit_hook`, `commit_msg_hook`, `prepare_commit_msg_hook` e `scan_history`; consultado em 2026-10-03.
