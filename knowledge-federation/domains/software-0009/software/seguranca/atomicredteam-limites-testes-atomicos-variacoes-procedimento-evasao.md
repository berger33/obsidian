---
id: software.seguranca.tranche12.001120
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

# Limites dos Testes Atômicos: **Ancoragem em Procedimentos (*Procedure-Level Anchoring*)** e Como Evitar Regras Frágeis de Linha de Comando

## Em uma frase
Existe uma armadilha clássica na Engenharia de Detecção que todo analista precisa conhecer ao usar o Atomic Red Team: **escrever uma regra de detecção que busca literalmente a string padrão do teste atômico (por exemplo, `CommandLine contains 'AtomicRedTeam'` ou o nome do arquivo default `lsass_dump.dmp`), obtendo 100% de aprovação no teste, mas 0% de detecção contra um atacante real que muda o nome do arquivo de saída!**

## Por que importa
Esse fenômeno é chamado de **Ancoragem em Procedimento (*Procedure-Level Anchoring*)**: lembre-se de que uma **Técnica** ou **Subtécnica** do MITRE ATT&CK (como `T1003.001` — *LSASS Memory*) pode ser executada por dezenas de **Procedimentos** diferentes (Mimikatz, ProcDump, `comsvcs.dll MiniDump`, Task Manager, Nanodump, HandleKatz, `SilentProcessExit`, acesso direto a `ntdll!NtReadVirtualMemory`)!

## Como funciona
Portanto, ao usar o Atomic Red Team para validar suas defesas, siga duas regras de engenharia: **(1) Varie sempre os `input_arguments` (`-InputArgs`)** ao testar suas regras (mude nomes de arquivos, caminhos e flags para garantir que a regra não depende dos defaults do Atomic Red Team); e **(2) Projete suas detecções o mais próximo possível do comportamento invariante do sistema operacional** (ex.: evento Sysmon `EventID 10 ProcessAccess` no `lsass.exe` com `GrantedAccess` suspeito, em vez de apenas o nome do executável na linha de comando)!

## Exemplo
```powershell
# Testar se a regra de deteccao sobrevive quando alteramos os input_arguments padrao do teste atomico via -InputArgs
$CustomArgs = @{
    "output_file" = "C:\ProgramData\diag_mem_report_99.bin"
}
Invoke-AtomicTest T1003.001 -TestNumbers 1 -InputArgs $CustomArgs
Invoke-AtomicTest T1003.001 -TestNumbers 1 -InputArgs $CustomArgs -Cleanup
```

## Limites e trade-offs
A pirâmide da dor (*Pyramid of Pain* de David Bianco) aplica-se diretamente aqui: regras que detectam apenas hashes, IPs ou flags estáticas de um único teste atômico são facilmente contornadas; regras que detectam a telemetria de comportamento subjacente da técnica protegem contra variações conhecidas e desconhecidas.

## Como verificar
Sempre execute todos os números de teste (`-TestNumbers 1,2,3...`) disponíveis dentro de uma mesma subtécnica `Txxxx.xxx` para medir sua cobertura através de múltiplos procedimentos distintos.

## Conexões
- [[atomicredteam-integracao-mitre-caldera-vectr-cobertura-attack-navigator]] — Veja também: Integração do **Atomic Red Team** com **MITRE Caldera**, **VECTR** e Camadas do **MITRE ATT&CK Navigator**.
- [[atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml]] — Referência cruzada direta com atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml.
- [[atomicredteam-anatomia-especificacao-yaml-input-arguments-executors-cleanup]] — Referência cruzada direta com atomicredteam-anatomia-especificacao-yaml-input-arguments-executors-cleanup.
- [[sigma-logica-detection-modificadores-valores-base64offset-windash-re]] — Referência cruzada direta com sigma-logica-detection-modificadores-valores-base64offset-windash-re.

## Fontes
- [Red Canary Atomic Red Team Official GitHub — Library of Tests Mapped to MITRE ATT&CK](https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md) — repositório oficial do Atomic Red Team com mais de 1.870 testes atômicos declarativos em YAML mapeados às técnicas do MITRE ATT&CK; consultado em 2026-10-03.
- [Red Canary `Invoke-AtomicRedTeam` Official GitHub — PowerShell Execution Framework](https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md) — documentação oficial do motor multiplataforma `Invoke-AtomicRedTeam` para Windows, Linux e macOS; consultado em 2026-10-03.
