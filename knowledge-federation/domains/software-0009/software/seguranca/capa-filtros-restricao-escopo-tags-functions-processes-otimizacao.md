---
id: software.seguranca.tranche13.001224
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/mandiant/capa/master/README.md", "https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Acelerando o `capa` em Binários Complexos: Filtros por Tag/Namespace (**`-t`**), Restrição por Endereço de Função (**`--restrict-to-functions`**) e Cache **`.viv`**

## Em uma frase
E quando você está analisando um binário gigante de 30 MB (com mais de 15.000 funções) ou só quer verificar rapidamente as regras de **Criptografia (`data-manipulation/encryption`)** ou **Anti-Análise (`anti-analysis`)** sobre duas funções específicas (`0x401200` e `0x401850`) que você acabou de encontrar no Ghidra?

## Por que importa
O `capa` possui três recursos de foco e aceleração cirúrgica: **(1) Filtro de Regras (`-t, --tag <texto>`)** — executa apenas as regras cujo nome, namespace, autor, ATT&CK ou MBC contenham a string informada (incluindo todas as dependências filhas necessárias!); **(2) Restrição por Endereço de Função (`--restrict-to-functions 0x401200,0x401850`)** — em vez de avaliar regras em todas as milhares de funções do binário, analisa exclusivamente as funções nos endereços virtuais listados!; e **(3) Cache do Workspace Vivisect (`export CAPA_SAVE_WORKSPACE=1`)**!

## Como funciona
Quando você define a variável de ambiente **`CAPA_SAVE_WORKSPACE=1`**, na primeira execução o `capa` salva no disco o arquivo de análise do motor desmontador (`binario.exe.viv`); nas execuções seguintes sobre o mesmo binário, o `capa` pula toda a fase pesada de desmontagem do CFG e carrega o `.viv` instantaneamente!

## Exemplo
```bash
# Salvar o workspace .viv em disco e rodar o capa restrito apenas a duas funcoes especificas e ao namespace de criptografia
export CAPA_SAVE_WORKSPACE=1
capa \
  -t data-manipulation/encryption \
  --restrict-to-functions 0x401200,0x401850 \
  -vv ./amostras/malware_grande.exe
```

## Limites e trade-offs
Ao analisar funções de inicialização (`.init` ou `DllMain`) que despacham chamadas para dezenas de funções filhas, lembre-se de que uma regra de escopo `file` pode depender de resultados de várias funções — portanto, use `--restrict-to-functions` especificamente quando estiver investigando capacidades no nível de `function` ou `basic block`.

## Como verificar
Para limpar os arquivos `.viv` após concluir a engenharia reversa do caso, basta removê-los da pasta de amostras (`rm -f ./amostras/*.viv`).

## Conexões
- [[capa-anatomia-regras-yaml-escopos-file-function-basic-block-instruction]] — Veja também: Anatomia das Regras YAML do **`capa-rules`**: Escopos Estáticos (**`file`, `function`, `basic block`, `instruction`**) e Operadores Lógicos (`and`, `or`, `count`, `optional`).
- [[capa-analise-multi-formato-pe-elf-dotnet-shellcode-assinaturas-flirt]] — Veja também: Análise Multi-Formato no `capa`: Executáveis **Windows PE**, **Linux ELF**, Assemblies **.NET (CIL)**, **Shellcode Bruto (`-f sc32`/`sc64`)** e Assinaturas **FLIRT (`-s`)**.
- [[capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant]] — Referência cruzada direta com capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant.
- [[capa-modos-saida-verbose-vv-enderecos-funcoes-json-automacao]] — Referência cruzada direta com capa-modos-saida-verbose-vv-enderecos-funcoes-json-automacao.
- [[floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded]] — Referência cruzada direta com floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded.

## Fontes
- [Mandiant FLARE `capa` Official GitHub — Detect Capabilities in Executable Files](https://raw.githubusercontent.com/mandiant/capa/master/README.md) — repositório oficial do Mandiant `capa` cobrindo identificação de capacidades em PE, ELF, .NET, shellcode e relatórios de sandbox mapeadas ao ATT&CK e MBC; consultado em 2026-10-03.
- [Mandiant `capa` Official Usage & Advanced Documentation (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md) — guia técnico oficial de uso do `capa` detalhando modos `-v`/`-vv`/`-j`, filtros `-t`, `--restrict-to-functions`, `--restrict-to-processes`, `CAPA_SAVE_WORKSPACE` e integrações IDA/Ghidra/Web; consultado em 2026-10-03.
