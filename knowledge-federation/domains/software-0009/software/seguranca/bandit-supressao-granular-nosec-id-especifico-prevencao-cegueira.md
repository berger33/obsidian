---
id: software.seguranca.tranche03.000263
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://bandit.readthedocs.io/en/latest/config.html", "https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst", "https://github.com/PyCQA/bandit"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Bandit Supressão Segura de Falsos Positivos (`# nosec B602, B607`): por que nunca usar `# nosec` genérico sem ID

## Em uma frase
Conforme explica a seção *Exclusions* da documentação oficial (`bandit.readthedocs.io/en/latest/config.html`), quando uma linha específica do código foi revisada pela equipe de segurança e representa um falso positivo aceitável, você deve suprimi-la especificando **explicitamente o ID ou nome do teste** no comentário (**`# nosec B602`** ou **`# nosec assert_used`**), em vez de um `# nosec` em branco.

## Por que importa
Se um desenvolvedor colocar um `# nosec` genérico sem ID em uma linha para silenciar um aviso menor (ex.: `B108` caminho `/tmp`) e meses depois outro desenvolvedor modificar aquela mesma linha introduzindo uma vulnerabilidade crítica de **Command Injection (`B602`)**, o `# nosec` genérico esconderá a nova vulnerabilidade crítica silenciosamente!

## Como funciona
Quando você escreve **`# nosec B108`**, o Bandit suprime naquela linha **apenas** o alerta `B108` e continua reportando normalmente qualquer outra vulnerabilidade que venha a surgir na mesma linha!

## Exemplo
```python
import subprocess

# CORRETO: suprime apenas os avisos B404/B603 revisados (argumentos estáticos sem shell=True),
# mantendo ativa a detecção se alguém adicionar shell=True (B602) no futuro:
proc = subprocess.run(["/usr/bin/git", "status"], check=True)  # nosec B603
```

## Limites e trade-offs
Durante auditorias periódicas de AppSec, você pode executar o Bandit com a flag **`--ignore-nosec` (`-i`)** para listar absolutamente todos os achados mesmo nas linhas que possuem comentários `# nosec`, revisando todas as exceções do repositório.

## Como verificar
Execute `bandit -r . --ignore-nosec` para auditar todos os pontos onde `# nosec` foi utilizado.

## Conexões
- [[bandit-configuracao-pyproject-toml-bandit-yaml-ini-tests-skips]] — Veja também: Bandit Configuração Declarativa (`pyproject.toml`, `bandit.yaml` e `.bandit`): controle de `exclude_dirs`, `tests` e `skips`.
- [[bandit-injecao-comandos-subprocess-shell-true-b602-b605-os-system]] — Veja também: Bandit Prevenção de Command Injection (`B602`–`B607`): `subprocess` com `shell=True`, `os.system` e customização do plugin.

## Fontes
- [PyCQA Bandit Official Documentation — Configuration (pyproject.toml, bandit.yaml, .bandit INI, Granular # nosec Exclusions & pre-commit Integration)](https://bandit.readthedocs.io/en/latest/config.html) — Documentação oficial de configuração do Bandit detalhando arquivos INI/YAML/TOML, exclusões por ID no comentário # nosec e customização de plugins; consultado em 2026-10-03.
- [PyCQA Bandit GitHub — README.rst (Python AST Security Linter Architecture, Sigstore Cosign Container Verification & References)](https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst) — README oficial do PyCQA/bandit apresentando a arquitetura de análise de nós AST em Python e verificação de imagens com Cosign; consultado em 2026-10-03.
- [PyCQA Bandit — Official GitHub Repository](https://github.com/PyCQA/bandit) — Repositório oficial Apache-2.0 do PyCQA Bandit; consultado em 2026-10-03.
