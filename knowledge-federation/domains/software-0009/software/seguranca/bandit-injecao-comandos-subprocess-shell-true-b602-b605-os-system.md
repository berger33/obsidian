---
id: software.seguranca.tranche03.000264
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

# Bandit Prevenção de Command Injection (`B602`–`B607`): `subprocess` com `shell=True`, `os.system` e customização do plugin

## Em uma frase
A família de plugins **`B602` (`subprocess_popen_with_shell_equals_true`)**, **`B605` (`start_process_with_a_shell`)**, **`B606` (`start_process_with_no_shell`)** e **`B607` (`start_process_with_partial_path`)** do Bandit inspeciona chamadas a processos externos no Python, diferenciando chamadas que invocam um interpretador de shell (`shell=True`, `os.system`, `os.popen`) de chamadas que executam argumentos diretamente via `execve` (`shell=False`).

## Por que importa
Quando `subprocess.Popen(cmd, shell=True)` ou `os.system(cmd)` recebe uma string interpolada com entrada do usuário (ex.: `f"ping -c 1 {host}"`), caracteres como `;`, `|`, `&&` ou `$(...)` permitem execução remota de comandos arbitrários (*OS Command Injection — CWE-78*).

## Como funciona
Conforme documentado em `config.html`, o plugin `any_other_function_with_shell_equals_true` permite inclusive customizar no `bandit.yaml` / `pyproject.toml` as listas `no_shell`, `shell` e `subprocess` para incluir wrappers internos da sua empresa que executam comandos!

## Exemplo
```python
import subprocess

def run_safe_ping(target_ip: str) -> bytes:
    # SEGURO contra injeção de metacaracteres de shell: lista de argumentos com shell=False (padrão) e caminho absoluto:
    return subprocess.check_output(["/bin/ping", "-c", "1", target_ip], shell=False, timeout=5)
```

## Limites e trade-offs
Mesmo com `shell=False`, o Bandit emite `B607` (`LOW`) se o primeiro argumento não for um caminho absoluto (ex.: `"ping"` em vez de `"/bin/ping"`), prevenindo ataques de *PATH Hijacking*.

## Como verificar
Teste rodar o Bandit sobre um arquivo com `subprocess.Popen(user_cmd, shell=True)` e confirme o disparo de `B602 (Severity: HIGH)`.

## Conexões
- [[bandit-supressao-granular-nosec-id-especifico-prevencao-cegueira]] — Veja também: Bandit Supressão Segura de Falsos Positivos (`# nosec B602, B607`): por que nunca usar `# nosec` genérico sem ID.
- [[bandit-desserializacao-insegura-pickle-yaml-load-marshal-b301-b506]] — Veja também: Bandit Desserialização Insegura e XML (`B301` `pickle`, `B506` `yaml.load`, `B314`–`B320` XXE `defusedxml`).

## Fontes
- [PyCQA Bandit Official Documentation — Configuration (pyproject.toml, bandit.yaml, .bandit INI, Granular # nosec Exclusions & pre-commit Integration)](https://bandit.readthedocs.io/en/latest/config.html) — Documentação oficial de configuração do Bandit detalhando arquivos INI/YAML/TOML, exclusões por ID no comentário # nosec e customização de plugins; consultado em 2026-10-03.
- [PyCQA Bandit GitHub — README.rst (Python AST Security Linter Architecture, Sigstore Cosign Container Verification & References)](https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst) — README oficial do PyCQA/bandit apresentando a arquitetura de análise de nós AST em Python e verificação de imagens com Cosign; consultado em 2026-10-03.
- [PyCQA Bandit — Official GitHub Repository](https://github.com/PyCQA/bandit) — Repositório oficial Apache-2.0 do PyCQA Bandit; consultado em 2026-10-03.
