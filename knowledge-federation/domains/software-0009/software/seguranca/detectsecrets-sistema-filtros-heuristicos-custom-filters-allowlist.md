---
id: software.seguranca.tranche11.001065
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md", "https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura de **Filtros Heurísticos (`filters_used`)**, Dicionários (**`--word-list`**), Exclusões Regex e **Allowlists Inline (`pragma: allowlist secret`)**

## Em uma frase
Por que o `detect-secrets` gera muito menos falsos positivos em código real do que um simples scanner de entropia de Shannon bruto? Porque todo achado emitido por um Plugin Detector passa por um pipeline em cascata de **Filtros Heurísticos Integrados (`detect_secrets.filters.*`)** antes de ser reportado!

## Por que importa
Veja o que os filtros nativos descartam automaticamente: **`is_sequential_string`** (descarta sequências óbvias como `abcdef123456` ou `1234567890`), **`is_potential_uuid`** (descarta UUIDs padrão `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`), **`is_likely_id_string`**, **`is_templated_secret`** (descarta placeholders como `${API_KEY}` ou `<SEGREDO>`), **`is_prefixed_with_dollar_sign`** (variáveis `$TOKEN`), **`is_indirect_reference`** (chamadas de função como `os.environ["SECRET"]`), **`is_lock_file`** e **`is_not_alphanumeric_string`**!

## Como funciona
Além disso, você pode passar um dicionário de palavras conhecidas via **`--word-list palavras.txt`** (para o filtro `should_exclude_secret` descartar hashes/strings que contenham termos de domínio), excluir arquivos/linhas por regex (`--exclude-files`, `--exclude-lines`, `--exclude-secrets`) ou marcar uma linha individual no código com o comentário oficial **`# pragma: allowlist secret`** (ou `// pragma: allowlist nextline secret`)!

## Exemplo
```bash
# Gerar o baseline excluindo arquivos de teste/fixtures por regex e fornecendo uma wordlist de falsos positivos conhecidos
detect-secrets scan \
  --exclude-files '^tests/fixtures/.*' \
  --exclude-lines 'MOCK_API_TOKEN' \
  --word-list /etc/secops/known-safe-terms.txt > .secrets.baseline
```

## Limites e trade-offs
Se você quiser rodar o `detect-secrets` em modo de conformidade estrita onde **apenas** as linhas que possuem o comentário explícito `# pragma: allowlist secret` são ignoradas, passe a flag **`--only-allowlisted`**!

## Como verificar
E para auditar se os desenvolvedores estão abusando do comentário `# pragma: allowlist secret` para esconder segredos reais, basta buscar no código (ou via `detect-secrets scan --force-use-all-plugins --disable-filter detect_secrets.filters.allowlist.is_line_allowlisted`) todas as ocorrências do pragma!

## Conexões
- [[detectsecrets-bloqueio-commits-detect-secrets-hook-pre-commit-cicd]] — Veja também: Bloqueio em Tempo Real com **`detect-secrets-hook`**: Integração com **Framework `pre-commit`** e Pipelines CI/CD (`git diff --staged` & `git ls-files`).
- [[detectsecrets-extensibilidade-api-python-secretscollection-custom-plugins]] — Veja também: API Python do `detect-secrets` (**`SecretsCollection` & `transient_settings`**): Criando **Plugins e Filtros Customizados (`file://...`)**.
- [[detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp]] — Referência cruzada direta com detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp.
- [[detectsecrets-plugins-detectores-entropia-base64-hex-keyword-cloud]] — Referência cruzada direta com detectsecrets-plugins-detectores-entropia-base64-hex-keyword-cloud.

## Fontes
- [Yelp `detect-secrets` Official GitHub — Enterprise Secret Detection, `.secrets.baseline`, Plugins & Filters](https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md) — documentação oficial do `detect-secrets` cobrindo `scan`, `audit`, `detect-secrets-hook`, os 27+ plugins detectores, filtros heurísticos e API Python `SecretsCollection`; consultado em 2026-10-03.
- [Yelp `detect-secrets` Official Pre-Commit Hook Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml) — especificação oficial do hook `detect-secrets-hook` para integração em pipelines e estações de desenvolvimento; consultado em 2026-10-03.
