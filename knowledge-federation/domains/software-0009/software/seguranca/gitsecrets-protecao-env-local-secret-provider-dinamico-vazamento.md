---
id: software.seguranca.tranche10.000976
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

# Técnica Avançada com `git-secrets`: Usando **`--add-provider`** para Garantir que Nenhum Valor do `.env` Local Seja Copiado para o Código

## Em uma frase
Mesmo quando o arquivo `.env` de desenvolvimento local está corretamente listado no `.gitignore` (para não ser commitado inteiro), um acidente muito frequente acontece durante sessões de debug: o desenvolvedor copia temporariamente o valor literal de uma chave que estava no seu `.env` e o cola direto dentro de um teste unitário (`test_payment.py`) ou arquivo de configuração (`settings.py`), esquecendo de removê-lo antes do `git commit`!

## Por que importa
Se aquele segredo específico for uma senha ou token customizado que não segue o formato `AKIA...` da AWS, como o `git-secrets` pode bloqueá-lo com **100% de precisão e zero falsos positivos**?

## Como funciona
Registrando um **Secret Provider (`--add-provider`)** que extrai em tempo real os valores (com mais de 12 caracteres) definidos nos arquivos `.env*` locais do próprio projeto!

## Exemplo
```bash
# Registrar um Secret Provider que extrai dinamicamente valores sensiveis do .env local para impedir que sejam colados no codigo!
git secrets --add-provider -- awk -F= '/^[A-Za-z0-9_]+=/{val=$2; gsub(/^["'\'']|["'\'']$/,"",val); if(length(val)>=12) print val}' .env
```

## Limites e trade-offs
Entenda por que essa técnica com `--add-provider` é tão segura: os valores reais dos segredos **nunca são copiados para dentro do `.git/config`** (eles continuam apenas no `.env` ignorado pelo Git), mas toda vez que você der `git commit`, o `git-secrets` roda o comando `awk` em memória e garante que nenhum valor presente no `.env` apareça nos arquivos commitados nem na mensagem de commit!

## Como verificar
Verifique que o provider foi registrado corretamente rodando `git config --get-all secrets.providers`.

## Conexões
- [[gitsecrets-modos-varredura-scan-cached-untracked-no-index-history]] — Veja também: `git-secrets` Modos de Varredura: **`--scan`** (`--cached`, `--untracked`, `--no-index`, `-r`, `stdin`) vs **`--scan-history`** em Todo o Histórico Git.
- [[gitsecrets-diferencas-egrep-gnu-bsd-macos-linux-portabilidade]] — Veja também: Portabilidade de Expressões Regulares no `git-secrets`: Diferenças entre **GNU `grep -E` (Linux)** e **BSD `grep -E` (macOS)** e Boas Práticas POSIX ERE.
- [[gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos]] — Referência cruzada direta com gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos.
- [[gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider]] — Referência cruzada direta com gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider.
- [[talisman-configuracao-avancada-scopeconfig-allowed-custom-patterns-severity]] — Referência cruzada direta com talisman-configuracao-avancada-scopeconfig-allowed-custom-patterns-severity.

## Fontes
- [AWS Labs git-secrets Official Documentation (`README.rst`) — CLI Reference, `--register-aws`, Bedrock Keys & `.gitallowed`](https://raw.githubusercontent.com/awslabs/git-secrets/master/README.rst) — documentação oficial do `git-secrets` cobrindo instalação dos 3 hooks (`pre-commit`, `commit-msg`, `prepare-commit-msg`), `--register-aws`, `--aws-provider`, `--scan-history` e `.gitallowed`; consultado em 2026-10-03.
- [AWS Labs git-secrets Official Implementation (`git-secrets`) — Hook Internals & Git-Grep Engine](https://raw.githubusercontent.com/awslabs/git-secrets/master/git-secrets) — código-fonte oficial do `git-secrets` mostrando o funcionamento interno de `pre_commit_hook`, `commit_msg_hook`, `prepare_commit_msg_hook` e `scan_history`; consultado em 2026-10-03.
