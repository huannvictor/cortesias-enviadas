# Defina o caminho da pasta onde os arquivos serão criados
$directoryPath = ".\cortesias"

# Crie a pasta se ela não existir
if (-not (Test-Path -Path $directoryPath)) {
    New-Item -ItemType Directory -Path $directoryPath
}

# Defina a quantidade de arquivos a serem criados
$quantidadeArquivos = 45

# Defina os códigos das escolas (exemplo: 101 a 200)
$codigosEscolas = 101..200

# Defina o ano e a extensão dos arquivos
$ano = "2025"
$extensao = "txt"

# Crie os arquivos
for ($i = 0; $i -lt $quantidadeArquivos; $i++) {
    $codigoEscola = $codigosEscolas[$i]
    $pagina = ($i % 10) + 1  # Gera páginas de 1 a 10
    $nomeArquivo = "$codigoEscola`_$ano`_$pagina.$extensao"
    $caminhoCompleto = Join-Path -Path $directoryPath -ChildPath $nomeArquivo

    # Cria um arquivo vazio
    New-Item -ItemType File -Path $caminhoCompleto
    Write-Host "Arquivo criado: $caminhoCompleto"
}

Write-Host "Concluído! $quantidadeArquivos arquivos foram criados em $directoryPath."