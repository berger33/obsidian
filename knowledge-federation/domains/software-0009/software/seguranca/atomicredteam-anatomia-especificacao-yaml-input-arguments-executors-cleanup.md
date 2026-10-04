---
id: software.seguranca.tranche12.001112
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md", "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Anatomia da Especificação YAML de um Teste Atômico: **`auto_generated_guid`**, **`input_arguments`**, **`dependencies`**, **`executor`** e **`cleanup_command`**

## Em uma frase
Para criar novos testes atômicos corporativos ou customizar parâmetros de execução sem quebrar a máquina de teste, é fundamental compreender os cinco blocos estruturais que compõem cada entrada em `atomic_tests` dentro de `Txxxx.yaml`!

## Por que importa
Primeiro, **`auto_generated_guid`** (um UUID v4 único por teste que permite invocar exatamente aquele procedimento via `-TestGuids` sem depender do número ou nome do teste); segundo, **`input_arguments`** (dicionário de variáveis tipadas `path`, `string`, `url` ou `integer` com valores `default`, interpoladas no comando via sintaxe **`#{nome_do_argumento}`**); e terceiro, **`dependencies`** (`description`, `prereq_command` que retorna `0` se o pré-requisito existe e `get_prereq_command` que baixa ou instala automaticamente a ferramenta necessária)!

## Como funciona
Quarto, o bloco **`executor`** define qual interpretador rodará o teste (`powershell`, `command_prompt`, `sh`, `bash` ou `manual`), se requer privilégio administrativo (**`elevation_required: true`**), o script de execução (**`command`**) e, quinto, o **`cleanup_command`** — que desfaz artefatos criados no sistema (apaga tarefas agendadas, chaves de registro, arquivos temporários ou contas de teste) após a validação da detecção!

## Exemplo
```yaml
# Estrutura de um teste atomico declarativo para criacao e limpeza de chave Run de persistencia (T1547.001)
- name: Reg Key Run Persistence - Atomic Test
  auto_generated_guid: d9f4b3a2-1c2e-4f5a-8b9c-0d1e2f3a4b5c
  description: Adiciona uma entrada de teste na chave CurrentVersion\Run do usuario atual
  supported_platforms:
    - windows
  input_arguments:
    command_to_execute:
      description: Executavel a ser registrado no Run
      type: path
      default: C:\Windows\System32\calc.exe
  executor:
    name: command_prompt
    elevation_required: false
    command: |
      REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "AtomicRedTeamTest" /t REG_SZ /F /D "#{command_to_execute}"
    cleanup_command: |
      REG DELETE "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "AtomicRedTeamTest" /f >nul 2>&1
```

## Limites e trade-offs
Regra de ouro ao escrever um `cleanup_command` no Atomic Red Team: torne-o **idempotente e silencioso** (por exemplo, `rm -f` no Linux ou `/f >nul 2>&1` no Windows) para que ele não retorne erro mesmo se o EDR tiver bloqueado o comando de ataque original antes da criação do artefato!

## Como verificar
Nunca hardcode caminhos ou IPs fixos dentro de `executor.command`: exponha-os sempre como `input_arguments` com valores padrão seguros.

## Conexões
- [[atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml]] — Veja também: Arquitetura do **Atomic Red Team (`redcanaryco/atomic-red-team`)**: Biblioteca Aberta de Testes Determinísticos Mapeados ao **MITRE ATT&CK**.
- [[atomicredteam-execucao-invoke-atomicredteam-powershell-showdetails-checkprereqs]] — Veja também: Motor de Execução **`Invoke-AtomicRedTeam`** (PowerShell Core Multiplataforma): `-ShowDetails`, `-CheckPrereqs`, `-GetPrereqs` e `-Cleanup`.
- [[atomicredteam-desenvolvimento-novos-atomics-validacao-ci-pre-commit]] — Referência cruzada direta com atomicredteam-desenvolvimento-novos-atomics-validacao-ci-pre-commit.

## Fontes
- [Red Canary Atomic Red Team Official GitHub — Library of Tests Mapped to MITRE ATT&CK](https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md) — repositório oficial do Atomic Red Team com mais de 1.870 testes atômicos declarativos em YAML mapeados às técnicas do MITRE ATT&CK; consultado em 2026-10-03.
- [Red Canary `Invoke-AtomicRedTeam` Official GitHub — PowerShell Execution Framework](https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md) — documentação oficial do motor multiplataforma `Invoke-AtomicRedTeam` para Windows, Linux e macOS; consultado em 2026-10-03.
