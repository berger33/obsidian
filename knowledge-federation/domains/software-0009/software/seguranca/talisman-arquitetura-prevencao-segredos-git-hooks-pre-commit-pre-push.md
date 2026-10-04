---
id: software.seguranca.tranche10.000961
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
fontes: ["https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md", "https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# **Thoughtworks Talisman (`thoughtworks/talisman`)**: Arquitetura dos **6 Detectores de Segredos** em Hooks Git (**`pre-commit` vs `pre-push`**)

## Em uma frase
Criado pela **Thoughtworks** (`thoughtworks/talisman`, licença MIT, escrito em Go), o **Talisman** é um guardião de estação de trabalho e CI/CD projetado para interceptar *changesets* Git **antes que chaves privadas, senhas, tokens de autorização ou arquivos sensíveis saiam da máquina do desenvolvedor**!

## Por que importa
Conforme documentado na seção `Validations` do `README.md` oficial, o Talisman executa **6 categorias complementares de detectores** sobre os arquivos modificados: **(1) `filename`** (bloqueia extensões e nomes de arquivos de chaves privadas/certificados como `*.pem`, `*.key`, `*.p12`, `*.pfx`, `id_rsa`, `.htpasswd`), **(2) `filesize`** (alerta sobre arquivos anormalmente grandes que possam conter dumps), **(3) `filecontent`** (expressões regulares para segredos, chaves AWS, Bearer tokens e senhas), **(4) `entropy`** (detecta strings de alta entropia de Shannon), **(5) `encoded values`** (decodifica e inspeciona segredos ofuscados em **Base64 e Hexadecimal**!) e **(6) `credit card numbers`** (validação Luhn)!

## Como funciona
Entenda a diferença operacional crítica entre os dois modos de hook (`-g` / `--githook`): como **`pre-commit`** (`talisman --githook pre-commit`), o Talisman analisa **apenas as linhas alteradas (`git diff --cached`)** do commit atual; já como **`pre-push`** (`talisman --githook pre-push`), ele analisa **o arquivo inteiro** em que houve mudança!

## Exemplo
```bash
# Verificar a versao do Talisman e executar manualmente a validacao do changeset staged atual como pre-commit hook
talisman --version
talisman --githook pre-commit
```

## Limites e trade-offs
Por que a própria documentação oficial do Talisman recomenda fortemente usá-lo como **`pre-commit`**? Porque bloquear o segredo **antes que o commit seja criado localmente** evita que o segredo entre no histórico local `.git/objects` (o que exigiria um `git reset` ou `git filter-repo` trabalhoso se só fosse descoberto na hora do `git push`)!

## Como verificar
Configure `export TALISMAN_SKIP_UPGRADE=true` em ambientes corporativos com controle estrito de versões de binários ou redes sem saída direta para o GitHub.

## Conexões
- [[talisman-governanca-checksum-sha256-talismanrc-ignore-detectors]] — Veja também: Talisman **`.talismanrc` & Checksum SHA-256 (`--checksum`)**: Por Que o Modelo de **Exceção Vinculada ao Hash** Impede Vazamentos Futuros em Arquivos Ignorados.
- [[talisman-instalacao-global-git-template-framework-pre-commit-husky]] — Referência cruzada direta com talisman-instalacao-global-git-template-framework-pre-commit-husky.

## Fontes
- [Thoughtworks Talisman Official GitHub — Secret Detection in Git Hooks, `.talismanrc` SHA-256 Checksums, Detectors & History Scanner](https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md) — documentação oficial do Talisman cobrindo os 6 detectores de validação, configuração `.talismanrc` por checksum SHA-256, `scopeconfig`, modo interativo e `--scan`; consultado em 2026-10-03.
- [Thoughtworks Talisman Official Pre-Commit Hooks Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml) — especificação oficial dos hooks `talisman-commit` e `talisman-push` em Go; consultado em 2026-10-03.
