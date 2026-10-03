---
id: software.seguranca.tranche11.001069
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

# Afundando Falsos Positivos do **`KeywordDetector`** no `detect-secrets`: Como Escrever Código e Testes Sem Disparar Alertas de Variáveis `password` / `secret` / `token`

## Em uma frase
Na prática diária com o `detect-secrets`, qual é o plugin que mais gera dúvidas entre os desenvolvedores? O **`KeywordDetector`**! Ele procura atribuições no código onde o nome da variável ou chave JSON/YAML contém palavras-chave sensíveis (`password`, `passwd`, `secret`, `api_key`, `apikey`, `token`, `auth`, `credentials`, `private_key`) seguidas de um valor literal entre aspas (`password = "valor"`).

## Por que importa
Quando o desenvolvedor escreve um arquivo de tradução/internacionalização (`i18n/pt-BR.json`: `"forgot_password_label": "Esqueceu sua senha?"`), um mapeamento de nome de coluna ou um teste unitário (`user.password = "test_user_pass_123"`), o `KeywordDetector` pode sinalizar a linha!

## Como funciona
Em vez de desativar o `KeywordDetector` inteiro (o que deixaria senhas reais em texto claro passarem!), aplique três boas práticas: **(1)** Exclua os arquivos de tradução `i18n` / `locales` via `--exclude-files 'locales/.*\.json$'`; **(2)** Em testes unitários, use constantes ou funções fábrica (`user.password = generate_fake_password()`) — que o filtro nativo `is_indirect_reference` reconhece automaticamente como seguro!; ou **(3)** Use `# pragma: allowlist secret` nos mocks estáticos!

## Exemplo
```python
# Comparacao de codigo em testes unitarios: atribuicao literal (sinalizada pelo KeywordDetector) vs referencia indireta ou pragma
def get_mock_credential() -> str:
    return "mock-value-for-unit-tests"  # pragma: allowlist secret


# 1. Seguro: o filtro nativo is_indirect_reference do detect-secrets sabe que chamadas de funcao nao sao literais hardcoded
api_token = get_mock_credential()

# 2. Seguro: linhas com pragma explicito sao permitidas pelo filtro de allowlist
db_password = "dummy_test_password_value"  # pragma: allowlist secret
```

## Limites e trade-offs
Compreender como o filtro `is_indirect_reference` e o `KeywordDetector` interagem melhora inclusive a qualidade do código de testes da equipe: centralizar a geração de credenciais falsas de teste em uma única fixture/helper (com 1 único `# pragma: allowlist secret`) evita espalhar centenas de strings mágicas pelos testes!

## Como verificar
Use `detect-secrets scan --string 'db_password = "valor"'` para demonstrar aos desenvolvedores em treinamentos de AppSec por que uma linha específica acionou o `KeywordDetector`.

## Conexões
- [[detectsecrets-deteccao-bypasses-auditoria-ci-cd-github-actions-sarif]] — Veja também: Detecção de Bypass (`git commit --no-verify`) no CI/CD com `detect-secrets`: Como Auditar tanto **Novos Segredos** quanto **Adições Não-Auditadas ao Baseline**.
- [[detectsecrets-estrategia-adocao-corporativa-brownfield-greenfield-git]] — Veja também: Estratégia de Adoção Corporativa (`Brownfield` vs `Greenfield`): Combinando **Yelp `detect-secrets`**, **Talisman**, **`git-secrets`**, **Gitleaks** e **TruffleHog**.
- [[detectsecrets-plugins-detectores-entropia-base64-hex-keyword-cloud]] — Referência cruzada direta com detectsecrets-plugins-detectores-entropia-base64-hex-keyword-cloud.
- [[detectsecrets-sistema-filtros-heuristicos-custom-filters-allowlist]] — Referência cruzada direta com detectsecrets-sistema-filtros-heuristicos-custom-filters-allowlist.
- [[detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp]] — Referência cruzada direta com detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp.

## Fontes
- [Yelp `detect-secrets` Official GitHub — Enterprise Secret Detection, `.secrets.baseline`, Plugins & Filters](https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md) — documentação oficial do `detect-secrets` cobrindo `scan`, `audit`, `detect-secrets-hook`, os 27+ plugins detectores, filtros heurísticos e API Python `SecretsCollection`; consultado em 2026-10-03.
- [Yelp `detect-secrets` Official Pre-Commit Hook Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml) — especificação oficial do hook `detect-secrets-hook` para integração em pipelines e estações de desenvolvimento; consultado em 2026-10-03.
